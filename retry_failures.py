import os
import csv
import argparse
import time
from generate_content import generate_summary, get_wikipedia_content, slugify, CONTENT_DIR, DEFAULT_MODEL

def main():
    parser = argparse.ArgumentParser(description='Retry failed mental model generations.')
    parser.add_argument('--model', type=str, default=DEFAULT_MODEL, help='Ollama model to use')
    args = parser.parse_args()

    failures_file = 'failures.txt'
    if not os.path.exists(failures_file):
        print("No failures.txt found.")
        return

    # Read failures
    failures_to_retry = []
    seen_slugs = set()
    
    # Get existing content slugs
    if os.path.exists(CONTENT_DIR):
        existing_files = os.listdir(CONTENT_DIR)
        existing_slugs = {f.replace('.md', '') for f in existing_files if f.endswith('.md')}
    else:
        existing_slugs = set()

    print(f"Found {len(existing_slugs)} existing generated models.")

    with open(failures_file, 'r') as f:
        # It seems the file format is Name,URL,ErrorType
        # But CSV reader might be safer if names contain commas. 
        # However, the previous script used f.write(f"{name},{wiki_url},...\n") which is naive CSV.
        # Let's try to parse it carefully.
        for line in f:
            parts = line.strip().split(',')
            if len(parts) < 3:
                continue
            
            # Find the part that starts with http to identify the URL
            url_index = -1
            for i, part in enumerate(parts):
                if part.strip().startswith('http'):
                    url_index = i
                    break
            
            if url_index == -1:
                print(f"Skipping malformed line: {line.strip()}")
                continue
                
            # Name is everything before URL
            name = ",".join(parts[:url_index]).strip()
            # URL is everything from start of URL to the last part (Error)
            # Wait, if URL has commas, it's split. 
            # The Error is the last part.
            # So URL is parts[url_index:-1] joined.
            url = ",".join(parts[url_index:-1]).strip()
            error_type = parts[-1].strip()
            
            slug = slugify(name)
            
            if slug in existing_slugs:
                print(f"Skipping {name} (already exists)")
                continue
                
            if slug in seen_slugs:
                continue
                
            seen_slugs.add(slug)
            failures_to_retry.append((name, url))

    print(f"Found {len(failures_to_retry)} actual missing entries to retry.")
    
    # Create a new failures file for this run to avoid appending duplicates to the old one?
    # Or just append to it? The user wants to clean it up.
    # Let's overwrite failures.txt with the remaining failures after this run?
    # For now, let's just process.
    
    new_failures = []

    for i, (name, wiki_url) in enumerate(failures_to_retry):
        print(f"[{i+1}/{len(failures_to_retry)}] Retrying: {name}")
        
        # 1. Get Wiki Content
        wiki_content = get_wikipedia_content(wiki_url)
        if not wiki_content:
            print(f"  - Failed to fetch Wikipedia content for {name}")
            new_failures.append((name, wiki_url, "Fetch Error"))
            continue
            
        # 2. Generate Summary
        summary = generate_summary(name, wiki_content, args.model, wiki_url)
        if not summary:
            print(f"  - Failed to generate summary for {name}")
            new_failures.append((name, wiki_url, "Generation Error"))
            continue
            
        # 3. Save
        slug = slugify(name)
        output_path = os.path.join(CONTENT_DIR, f"{slug}.md")
        with open(output_path, 'w') as f:
            f.write(f"# {name}\n\n")
            f.write(summary)
            
        print(f"  - Saved to {output_path}")
        time.sleep(0.5)

    # Update failures.txt with only the ones that failed AGAIN
    if new_failures:
        print(f"Writing {len(new_failures)} persistent failures to failures.txt")
        with open(failures_file, 'w') as f:
            for name, url, error in new_failures:
                f.write(f"{name},{url},{error}\n")
    else:
        print("All retries successful! Clearing failures.txt")
        open(failures_file, 'w').close()

if __name__ == "__main__":
    main()
