import csv
import urllib.request
import urllib.parse
import json
import time

INPUT_FILE = 'Master_Mental_Models_List.csv'
OUTPUT_FILE = 'Master_Mental_Models_List_Updated.csv'
USER_AGENT = 'MentalModelBot/1.0 (test@example.com)'

def get_wikipedia_url(term):
    """Fetches the closest Wikipedia article URL for a given term."""
    try:
        encoded_term = urllib.parse.quote(term)
        url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={encoded_term}&limit=1&namespace=0&format=json"
        headers = {'User-Agent': USER_AGENT}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            # data format: [search_term, [titles], [descriptions], [links]]
            if len(data) > 3 and data[3]:
                return data[3][0]
    except Exception as e:
        print(f"Error fetching URL for '{term}': {e}")
    return ""

def process_csv():
    print("Reading CSV...")
    rows = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    print(f"Total rows: {len(rows)}")

    # Identify duplicates
    seen_models = set()
    duplicates = set()
    
    # First pass to identify duplicates based on normalized name
    for row in rows:
        model_name = row['Mental Model'].strip().lower()
        if model_name in seen_models:
            duplicates.add(model_name)
        else:
            seen_models.add(model_name)

    # Add new columns
    new_fieldnames = fieldnames + ['Is Duplicate', 'Wikipedia URL']
    
    print("Processing rows...")
    processed_rows = []
    for i, row in enumerate(rows):
        model_name = row['Mental Model']
        normalized_name = model_name.strip().lower()
        
        # Mark duplicate
        is_duplicate = 'Yes' if normalized_name in duplicates and rows.index(row) != next(idx for idx, r in enumerate(rows) if r['Mental Model'].strip().lower() == normalized_name) else 'No'
        # Actually, the requirement is just to mark them. Let's mark all occurrences as duplicates if they appear more than once? 
        # Or usually "mark duplicates" means mark the subsequent ones. 
        # Let's stick to marking subsequent ones as duplicates, or maybe just flag if it IS a duplicate entry (i.e. appears multiple times).
        # The prompt says "Mark an duplicates (do not remove them)".
        # I will mark the second occurrence onwards as "Yes".
        
        # Wait, my logic above `rows.index(row) != next(...)` is a bit complex and O(N^2) inside the loop if not careful.
        # Let's redo the duplicate logic to be simpler and strictly mark 2nd+ occurrences.
        
        # We need to fetch Wikipedia URL
        print(f"[{i+1}/{len(rows)}] Processing: {model_name}")
        wiki_url = get_wikipedia_url(model_name)
        
        row['Is Duplicate'] = '' # Will fill in a second pass or just fix logic below
        row['Wikipedia URL'] = wiki_url
        processed_rows.append(row)
        
        # Be nice to the API
        time.sleep(0.1)

    # Correct duplicate marking logic
    seen_models_count = {}
    final_rows = []
    for row in processed_rows:
        model_name = row['Mental Model'].strip().lower()
        if model_name in seen_models_count:
            row['Is Duplicate'] = 'Yes'
        else:
            row['Is Duplicate'] = 'No'
            seen_models_count[model_name] = 1
        final_rows.append(row)

    print("Writing output CSV...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(final_rows)
    
    print("Done!")

if __name__ == "__main__":
    process_csv()
