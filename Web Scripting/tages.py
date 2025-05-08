from bs4 import BeautifulSoup
import requests

# URL of the website to scrape
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all product containers
    product_containers = soup.find_all('div', class_="col-md-4 col-xl-4 col-lg-4")
    
    # Loop through each product container and extract details
    for product in product_containers:
        # Extract price
        price_tag = product.find('span', {"itemprop": "price"})
        price = price_tag.text if price_tag else "N/A"
        
        # Extract description
        description_tag = product.find('p', {'class': 'description card-text'})
        description = description_tag.text if description_tag else "N/A"
        
        # Extract product name
        name_tag = product.find('a', {'class': 'title'})
        name = name_tag.text.strip() if name_tag else "N/A"
        
        # Extract review count
        review_tag = product.find('span', {"itemprop": "reviewCount"})
        reviews = review_tag.text if review_tag else "N/A"
        
        # Print the extracted details
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Description: {description}")
        print(f"Reviews: {reviews}")
        print("-" * 40)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
