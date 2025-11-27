import pandas as pd
import os

def filter_models():
    input_file = 'Master_Mental_Models_List_Updated.csv'
    output_file = 'mental_models_wiki.csv'

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    try:
        df = pd.read_csv(input_file)
        
        # Filter rows where 'Wikipedia URL' is not null and not empty
        # We also want to ensure it looks like a valid URL (starts with http)
        df_wiki = df[df['Wikipedia URL'].notna() & df['Wikipedia URL'].str.startswith('http', na=False)]
        
        print(f"Found {len(df_wiki)} entries with Wikipedia URLs.")
        
        df_wiki.to_csv(output_file, index=False)
        print(f"Saved filtered list to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filter_models()
