import requests
from bs4 import BeautifulSoup
import os


# URL variable
url = "https://www.amazon.in"

# Function to save the result to a file
def save_to_file(url, relative_path):
    try:
        # Get the absolute path relative to the script's directory
        
        # Get the directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Base directory: {base_dir}")
        
        # Construct the full path
        full_path = os.path.join(base_dir, relative_path)
        
        result = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        result.raise_for_status()  # Raise an error for bad status codes
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Write the content to the file
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(result.text)
        print(f"Data saved successfully to {full_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Data store in file
save_to_file(url, "data/amazon.html")