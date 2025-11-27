import pandas as pd
import requests
import os
import json
import re
import time
import argparse
from urllib.parse import urlparse

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3.1"
CONTENT_DIR = "content"

def get_wikipedia_content(url):
    """
    Fetches Wikipedia content using the API or scraping.
    For simplicity, we'll try to use the Wikipedia API via the 'wikipedia-api' library if possible,
    or just raw requests if we want full HTML. 
    Let's use the 'wikipedia-api' library wrapper which we installed.
    """
    import wikipediaapi
    
    # Extract title from URL
    # URL format: https://en.wikipedia.org/wiki/Title
    from urllib.parse import unquote
    path = urlparse(url).path
    # Decode the path (e.g. %27 -> ') and replace underscores
    title = unquote(path.split('/')[-1]).replace('_', ' ')
    
    wiki_wiki = wikipediaapi.Wikipedia('MentalModelsProject/1.0 (bot@example.com)', 'en')
    page = wiki_wiki.page(title)
    
    if page.exists():
        return page.text
    else:
        return None

def generate_summary(name, wiki_content, model, wiki_url):
    """
    Generates a summary using Ollama.
    """
    prompt = f"""You are an expert educator and writer. Your task is to write a comprehensive, engaging, and detailed summary of the mental model "{name}".
    
    The summary should be approximately 1000 words long.
    
    Structure the summary as follows:
    1.  **Introduction**: Define the mental model clearly and explain why it matters.
    2.  **Core Concept**: Explain the mechanism or theory behind it in depth.
    3.  **Examples**: Provide at least 3 concrete, real-world examples of this model in action (business, life, history, etc.).
    4.  **Application**: How can the reader apply this mental model in their daily life or decision making?
    5.  **Related Models**: Briefly mention 2-3 other mental models that are related or complementary. **IMPORTANT**: When mentioning these models, format them as markdown links like `[Model Name](/models/model-slug)`. You can guess the slug by lowercasing and replacing spaces with dashes.
    6.  **References**: Provide the source link.
    
    Use the following Wikipedia content as a primary source, but feel free to synthesize it with your general knowledge to make it engaging.
    
    Wikipedia Content:
    {wiki_content[:15000]}  # Limit context to avoid context window issues if too large
    
    Output in Markdown format.
    
    At the very end, add a "References" section with the following link:
    - [Wikipedia Entry]({wiki_url})
    """
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
        response.raise_for_status()
        return response.json().get('response', '')
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return None

def slugify(text):
    text = text.lower()
    return re.sub(r'[\W_]+', '-', text).strip('-')

def main():
    parser = argparse.ArgumentParser(description='Generate mental model summaries.')
    parser.add_argument('--model', type=str, default=DEFAULT_MODEL, help='Ollama model to use')
    parser.add_argument('--limit', type=int, default=None, help='Limit number of entries to process')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing files')
    args = parser.parse_args()

    if not os.path.exists(CONTENT_DIR):
        os.makedirs(CONTENT_DIR)

    input_file = 'mental_models_wiki.csv'
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Run filter_models.py first.")
        return

    df = pd.read_csv(input_file)
    
    if args.limit:
        df = df.head(args.limit)

    print(f"Processing {len(df)} entries using model '{args.model}'...")

    for index, row in df.iterrows():
        name = row['Mental Model']
        wiki_url = row['Wikipedia URL']
        
        slug = slugify(name)
        output_path = os.path.join(CONTENT_DIR, f"{slug}.md")
        
        if os.path.exists(output_path) and not args.overwrite:
            print(f"Skipping {name} (already exists)")
            continue
            
        print(f"[{index+1}/{len(df)}] Processing: {name}")
        
        # 1. Get Wiki Content
        wiki_content = get_wikipedia_content(wiki_url)
        if not wiki_content:
            print(f"  - Failed to fetch Wikipedia content for {name}")
            with open('failures.txt', 'a') as f:
                f.write(f"{name},{wiki_url},Fetch Error\n")
            continue
            
        # 2. Generate Summary
        summary = generate_summary(name, wiki_content, args.model, wiki_url)
        if not summary:
            print(f"  - Failed to generate summary for {name}")
            with open('failures.txt', 'a') as f:
                f.write(f"{name},{wiki_url},Generation Error\n")
            continue
            
        # 3. Save
        with open(output_path, 'w') as f:
            f.write(f"# {name}\n\n")
            f.write(summary)
            
        print(f"  - Saved to {output_path}")
        
        # Sleep briefly to be nice to system resources?
        time.sleep(0.5)

if __name__ == "__main__":
    main()
