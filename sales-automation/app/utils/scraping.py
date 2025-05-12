import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
import time
import random
from urllib.parse import urljoin
from datetime import datetime

class WebScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {'User-Agent': self.ua.random}
        
    def scrape_google(self, query, pages=3):
        """Scrape Google search results for companies"""
        results = []
        base_url = "https://www.google.com/search"
        
        for page in range(pages):
            params = {
                'q': query,
                'start': page * 10
            }
            
            try:
                response = requests.get(base_url, headers=self.headers, params=params)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for result in soup.find_all('div', class_='tF2Cxc'):
                    link = result.find('a')['href']
                    title = result.find('h3').text
                    
                    company_info = {
                        'company_name': title.split(' - ')[0],
                        'website': link,
                        'source': 'Google'
                    }
                    results.append(company_info)
                    
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                print(f"Error scraping Google: {e}")
                
        return results
    
    def scrape_linkedin(self, search_url):
        """Scrape LinkedIn company pages (Note: LinkedIn is difficult to scrape)"""
        results = []
        try:
            response = requests.get(search_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example extraction - actual selectors will vary
            companies = soup.find_all('div', class_='entity-result')
            
            for company in companies:
                name = company.find('span', {'dir': 'ltr'}).text.strip()
                industry = company.find('div', class_='entity-result__primary-subtitle').text.strip()
                location = company.find('div', class_='entity-result__secondary-subtitle').text.strip()
                
                company_info = {
                    'company_name': name,
                    'industry': industry,
                    'location': location,
                    'source': 'LinkedIn'
                }
                results.append(company_info)
                
            time.sleep(random.uniform(2, 5))
            
        except Exception as e:
            print(f"Error scraping LinkedIn: {e}")
            
        return results
    
    def export_to_excel(self, leads_data, filename='leads.xlsx'):
        """Export leads data to Excel"""
        df = pd.DataFrame(leads_data)
        df.to_excel(filename, index=False)
        return filename