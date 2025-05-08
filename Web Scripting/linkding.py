import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def create_folder(folder_name: str) -> None:
    """Create a directory if it doesn't exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"✅ Folder '{folder_name}' created successfully.")
    else:
        print(f"📁 Folder '{folder_name}' already exists.")

def initialize_browser() -> webdriver.Chrome:
    """Initialize and configure Chrome browser in headless mode."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    service = Service(executable_path=r"C:\Users\jigne\OneDrive\Documents\MCA\Company\Python\Web Scripting\driver\chromedriver.exe")
    return webdriver.Chrome(service=service, options=chrome_options)

def login_to_linkedin(browser: webdriver.Chrome, username: str, password: str) -> bool:
    """Log in to LinkedIn using provided credentials."""
    browser.get("https://www.linkedin.com/login")
    time.sleep(5)  # Wait for page to load

    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)  # Wait for login to complete

    if "feed" in browser.current_url:
        print("✅ Login successful!")
        return True
    else:
        print("❌ Login failed - check credentials or page structure")
        return False

def scrape_linkedin_feed(browser: webdriver.Chrome) -> str:
    """Scrape content from LinkedIn feed page."""
    browser.get("https://www.linkedin.com/feed/")
    time.sleep(5)  # Wait for feed to load
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    return browser.page_source

def save_content(content: str, folder_name: str, file_name: str) -> None:
    """Save scraped content to file."""
    file_path = os.path.join(folder_name, file_name)
    soup = BeautifulSoup(content, 'html.parser')
    pretty_content = soup.prettify()

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(pretty_content)
    print(f"💾 Content successfully saved to {file_path}")

def main():
    """Main execution function."""
    OUTPUT_FOLDER = "deta"
    OUTPUT_FILE = "linkedin_feed.html"

    username = input("Enter your LinkedIn email/username: ").strip()
    password = input("Enter your LinkedIn password: ").strip()

    create_folder(OUTPUT_FOLDER)
    browser = initialize_browser()

    try:
        if login_to_linkedin(browser, username, password):
            content = scrape_linkedin_feed(browser)
            save_content(content, OUTPUT_FOLDER, OUTPUT_FILE)
        else:
            print("🔴 Login failed. Exiting.")
    finally:
        # browser.quit()
        # print("🛑 Browser session closed")
        print("complet")

if __name__ == "__main__":
    main()
