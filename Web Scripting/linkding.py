import os
import time
import json
import requests
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame, ttk, Scrollbar, Text, END
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from bs4 import BeautifulSoup
from datetime import datetime
import traceback
import webbrowser
import re
from urllib.parse import urljoin

class LinkedInScraper:
    def __init__(self):
        self.driver = None
        self.logged_in = False
        self.output_folder = "linkedin_data"
        self.current_data = {}
        self.max_wait_time = 30
        self.request_timeout = 10
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def initialize_browser(self) -> bool:
        """Initialize Chrome browser"""
        try:
            chrome_options = Options()
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
            chrome_options.add_argument("--start-maximized")

            driver_path = self.find_chromedriver()
            if not driver_path:
                raise FileNotFoundError("ChromeDriver not found")
            
            service = Service(executable_path=driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.implicitly_wait(10)
            return True
        except Exception as e:
            print(f"Browser initialization error: {str(e)}")
            return False

    def find_chromedriver(self):
        """Find ChromeDriver in common locations"""
        common_paths = [
            r"C:\Users\jigne\OneDrive\Documents\MCA\Company\Python\Web Scripting\driver\chromedriver.exe",
            r"C:\chromedriver\chromedriver.exe",
            "/usr/local/bin/chromedriver",
            "/usr/bin/chromedriver"
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                return path
        return None

    def login_to_linkedin(self, username: str, password: str) -> bool:
        """Login to LinkedIn"""
        if not self.driver:
            if not self.initialize_browser():
                return False

        try:
            self.driver.get("https://www.linkedin.com/login")
            
            try:
                WebDriverWait(self.driver, self.max_wait_time).until(
                    EC.presence_of_element_located((By.ID, "username")))
                WebDriverWait(self.driver, self.max_wait_time).until(
                    EC.presence_of_element_located((By.ID, "password")))
            except TimeoutException:
                print("Login page elements not found")
                return False

            username_field = self.driver.find_element(By.ID, "username")
            username_field.clear()
            username_field.send_keys(username)
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

            try:
                WebDriverWait(self.driver, self.max_wait_time).until(
                    lambda driver: (
                        "feed" in driver.current_url.lower() or
                        "login-submit" in driver.current_url.lower() or
                        "checkpoint/challenge" in driver.current_url.lower()
                    ))
                
                if "feed" in self.driver.current_url.lower():
                    self.logged_in = True
                    return True
                else:
                    return False
            except TimeoutException:
                print("Login timeout")
                return False
        except Exception as e:
            print(f"Login error: {str(e)}")
            return False

    def search_linkedin(self, query: str, search_type: str, location: str = None, max_results: int = 50) -> dict:
        """Search LinkedIn with optional location filter"""
        if not self.logged_in:
            return {"error": "Not logged in"}
        
        search_types = ["people", "companies", "jobs", "posts"]
        if search_type not in search_types:
            return {"error": "Invalid search type"}
        
        try:
            base_url = f"https://www.linkedin.com/search/results/{search_type}/?keywords={query}"
            if location:
                base_url += f"&location={location}"
            
            self.driver.get(base_url)
            
            try:
                WebDriverWait(self.driver, self.max_wait_time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))
            except TimeoutException:
                return {"error": "Search results did not load"}

            # Scroll to load more results
            loaded_results = 0
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            
            while loaded_results < max_results:
                # Scroll down
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                
                # Check if we've reached the end
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                
                # Count current results
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                current_results = len(soup.find_all("li", class_="reusable-search__result-container"))
                if current_results > loaded_results:
                    loaded_results = current_results
                else:
                    break
                
                if loaded_results >= max_results:
                    break
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = []
            
            for result in soup.find_all("li", class_="reusable-search__result-container")[:max_results]:
                try:
                    if search_type == "people":
                        profile_url = self._extract_attribute(result, "a.app-aware-link", "href")
                        profile_data = self.scrape_profile(profile_url) if profile_url else {}
                        
                        result_data = {
                            "name": self._clean_text(self._extract_text(result, "span.entity-result__title-text")),
                            "title": self._clean_text(self._extract_text(result, "div.entity-result__primary-subtitle")),
                            "location": self._clean_text(self._extract_text(result, "div.entity-result__secondary-subtitle")),
                            "profile_url": profile_url,
                            "profile_details": profile_data
                        }
                    elif search_type == "companies":
                        company_url = self._extract_attribute(result, "a.app-aware-link", "href")
                        company_data = self.scrape_company(company_url) if company_url else {}
                        
                        result_data = {
                            "name": self._clean_text(self._extract_text(result, "span.entity-result__title-text")),
                            "industry": self._clean_text(self._extract_text(result, "div.entity-result__primary-subtitle")),
                            "location": self._clean_text(self._extract_text(result, "div.entity-result__secondary-subtitle")),
                            "profile_url": company_url,
                            "company_details": company_data
                        }
                    elif search_type == "jobs":
                        job_url = self._extract_attribute(result, "a.app-aware-link", "href")
                        job_data = self.scrape_job(job_url) if job_url else {}
                        
                        result_data = {
                            "title": self._clean_text(self._extract_text(result, "span.entity-result__title-text")),
                            "company": self._clean_text(self._extract_text(result, "div.entity-result__primary-subtitle")),
                            "location": self._clean_text(self._extract_text(result, "div.entity-result__secondary-subtitle")),
                            "time": self._clean_text(self._extract_text(result, "div.entity-result__insights")),
                            "job_url": job_url,
                            "job_details": job_data
                        }
                    elif search_type == "posts":
                        post_url = self._extract_attribute(result, "a.app-aware-link", "href")
                        post_data = self.scrape_post(post_url) if post_url else {}
                        
                        result_data = {
                            "author": self._clean_text(self._extract_text(result, "span.entity-result__title-text")),
                            "content": self._clean_text(self._extract_text(result, "div.entity-result__primary-subtitle")),
                            "time": self._clean_text(self._extract_text(result, "div.entity-result__secondary-subtitle")),
                            "post_url": post_url,
                            "post_details": post_data
                        }
                    
                    results.append(result_data)
                except Exception as e:
                    print(f"Result processing error: {str(e)}")
                    continue
            
            self.current_data[search_type] = results
            return {
                "success": True,
                "data": results,
                "stats": {
                    "total_results": len(results),
                    "query": query,
                    "type": search_type,
                    "location": location,
                    "timestamp": datetime.now().isoformat()
                }
            }
        except Exception as e:
            return {
                "error": "Search failed",
                "details": str(e),
                "traceback": traceback.format_exc()
            }

    def scrape_profile(self, profile_url: str) -> dict:
        """Scrape detailed profile information"""
        if not profile_url:
            return {}
        
        try:
            if not profile_url.startswith("http"):
                profile_url = urljoin("https://www.linkedin.com", profile_url)
            
            self.driver.get(profile_url)
            time.sleep(2)  # Wait for page to load
            
            # Scroll to load all sections
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Basic info
            name = self._clean_text(self._extract_text(soup, "h1.text-heading-xlarge"))
            headline = self._clean_text(self._extract_text(soup, "div.text-body-medium"))
            location = self._clean_text(self._extract_text(soup, "span.text-body-small.inline"))
            
            # About section
            about = self._clean_text(self._extract_text(soup, "div.display-flex.ph5.pv3"))
            
            # Experience
            experience = []
            for exp in soup.select("section.experience-section ul.pv-profile-section__section-info li"):
                try:
                    exp_data = {
                        "title": self._clean_text(self._extract_text(exp, "h3.t-16.t-black.t-bold")),
                        "company": self._clean_text(self._extract_text(exp, "p.pv-entity__secondary-title")),
                        "duration": self._clean_text(self._extract_text(exp, "span.pv-entity__bullet-item")),
                        "description": self._clean_text(self._extract_text(exp, "div.pv-entity__extra-details")),
                        "location": self._clean_text(self._extract_text(exp, "span.pv-entity__location"))
                    }
                    experience.append(exp_data)
                except:
                    continue
            
            # Education
            education = []
            for edu in soup.select("section.education-section ul.pv-profile-section__section-info li"):
                try:
                    edu_data = {
                        "school": self._clean_text(self._extract_text(edu, "h3.t-16.t-black.t-bold")),
                        "degree": self._clean_text(self._extract_text(edu, "p.pv-entity__secondary-title")),
                        "field": self._clean_text(self._extract_text(edu, "p.pv-entity__facet")),
                        "duration": self._clean_text(self._extract_text(edu, "span.pv-entity__dates"))
                    }
                    education.append(edu_data)
                except:
                    continue
            
            # Skills
            skills = []
            for skill in soup.select("section.skills-section ol.pv-skill-categories-section li"):
                try:
                    skill_data = {
                        "name": self._clean_text(self._extract_text(skill, "span.pv-skill-category-entity__name-text")),
                        "endorsements": self._clean_text(self._extract_text(skill, "span.pv-skill-category-entity__endorsement-count"))
                    }
                    skills.append(skill_data)
                except:
                    continue
            
            # Contact info (if available)
            contact_info = {}
            try:
                contact_button = self.driver.find_element(By.XPATH, "//a[contains(@href, 'contact-info')]")
                if contact_button:
                    contact_button.click()
                    time.sleep(2)
                    
                    contact_soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                    
                    # Email
                    email = self._clean_text(self._extract_text(contact_soup, "section.ci-email a.pv-contact-info__contact-link"))
                    
                    # Phone
                    phone = self._clean_text(self._extract_text(contact_soup, "section.ci-phone a.pv-contact-info__contact-link"))
                    
                    # Websites
                    websites = []
                    for site in contact_soup.select("section.ci-websites li"):
                        websites.append({
                            "url": self._extract_attribute(site, "a", "href"),
                            "label": self._clean_text(self._extract_text(site, "span.pv-contact-info__contact-link"))
                        })
                    
                    contact_info = {
                        "email": email,
                        "phone": phone,
                        "websites": websites
                    }
                    
                    # Close contact info modal
                    close_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
                    if close_button:
                        close_button.click()
                        time.sleep(1)
            except:
                pass
            
            return {
                "basic_info": {
                    "name": name,
                    "headline": headline,
                    "location": location,
                    "about": about
                },
                "experience": experience,
                "education": education,
                "skills": skills,
                "contact_info": contact_info,
                "profile_url": profile_url,
                "scraped_at": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Profile scraping error: {str(e)}")
            return {
                "error": "Profile scraping failed",
                "details": str(e)
            }

    def scrape_company(self, company_url: str) -> dict:
        """Scrape detailed company information"""
        if not company_url:
            return {}
        
        try:
            if not company_url.startswith("http"):
                company_url = urljoin("https://www.linkedin.com", company_url)
            
            self.driver.get(company_url)
            time.sleep(2)
            
            # Scroll to load all sections
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Basic info
            name = self._clean_text(self._extract_text(soup, "h1.org-top-card-summary__title"))
            industry = self._clean_text(self._extract_text(soup, "div.org-top-card-summary__industry"))
            location = self._clean_text(self._extract_text(soup, "div.org-top-card-summary__info-item"))
            website = self._clean_text(self._extract_text(soup, "a.org-top-card-summary__website"))
            size = self._clean_text(self._extract_text(soup, "div.org-about-company-module__company-size-definition-text"))
            founded = self._clean_text(self._extract_text(soup, "div.org-about-company-module__founded"))
            
            # About
            about = self._clean_text(self._extract_text(soup, "p.org-about-us-organization-description__text"))
            
            # Specialties
            specialties = []
            for spec in soup.select("div.org-about-company-module__specialities p"):
                specialties.append(self._clean_text(spec.get_text()))
            
            # Employees on LinkedIn
            employees = []
            try:
                see_all_employees = self.driver.find_element(By.XPATH, "//a[contains(@href, 'people')]")
                if see_all_employees:
                    see_all_employees.click()
                    time.sleep(2)
                    
                    # Scroll to load more employees
                    last_height = self.driver.execute_script("return document.body.scrollHeight")
                    while True:
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(1)
                        new_height = self.driver.execute_script("return document.body.scrollHeight")
                        if new_height == last_height:
                            break
                        last_height = new_height
                    
                    employee_soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                    
                    for emp in employee_soup.select("li.org-people-profile-card__profile-card"):
                        try:
                            emp_data = {
                                "name": self._clean_text(self._extract_text(emp, "h3.org-people-profile-card__profile-title")),
                                "title": self._clean_text(self._extract_text(emp, "div.org-people-profile-card__profile-subtitle")),
                                "location": self._clean_text(self._extract_text(emp, "div.org-people-profile-card__location")),
                                "profile_url": self._extract_attribute(emp, "a", "href")
                            }
                            employees.append(emp_data)
                        except:
                            continue
                    
                    # Go back to company page
                    self.driver.back()
                    time.sleep(2)
            except:
                pass
            
            return {
                "basic_info": {
                    "name": name,
                    "industry": industry,
                    "location": location,
                    "website": website,
                    "size": size,
                    "founded": founded
                },
                "about": about,
                "specialties": specialties,
                "employees_sample": employees[:10],  # Limit to first 10 employees
                "company_url": company_url,
                "scraped_at": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Company scraping error: {str(e)}")
            return {
                "error": "Company scraping failed",
                "details": str(e)
            }

    def scrape_job(self, job_url: str) -> dict:
        """Scrape detailed job information"""
        if not job_url:
            return {}
        
        try:
            if not job_url.startswith("http"):
                job_url = urljoin("https://www.linkedin.com", job_url)
            
            self.driver.get(job_url)
            time.sleep(2)
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Basic info
            title = self._clean_text(self._extract_text(soup, "h1.top-card-layout__title"))
            company = self._clean_text(self._extract_text(soup, "a.topcard__org-name-link"))
            location = self._clean_text(self._extract_text(soup, "span.topcard__flavor--bullet"))
            posted = self._clean_text(self._extract_text(soup, "span.posted-time-ago__text"))
            applicants = self._clean_text(self._extract_text(soup, "span.num-applicants__caption"))
            
            # Show more details
            try:
                show_more = self.driver.find_element(By.XPATH, "//button[contains(@class, 'show-more-less-html__button')]")
                if show_more:
                    show_more.click()
                    time.sleep(1)
                    soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            except:
                pass
            
            # Description
            description = self._clean_text(self._extract_text(soup, "div.show-more-less-html__markup"))
            
            # Criteria
            criteria = {}
            for item in soup.select("li.description__job-criteria-item"):
                key = self._clean_text(self._extract_text(item, "h3.description__job-criteria-subheader"))
                value = self._clean_text(self._extract_text(item, "span.description__job-criteria-text"))
                if key and value:
                    criteria[key.lower().replace(" ", "_")] = value
            
            return {
                "title": title,
                "company": company,
                "location": location,
                "posted": posted,
                "applicants": applicants,
                "description": description,
                "criteria": criteria,
                "job_url": job_url,
                "scraped_at": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Job scraping error: {str(e)}")
            return {
                "error": "Job scraping failed",
                "details": str(e)
            }

    def scrape_post(self, post_url: str) -> dict:
        """Scrape detailed post information"""
        if not post_url:
            return {}
        
        try:
            if not post_url.startswith("http"):
                post_url = urljoin("https://www.linkedin.com", post_url)
            
            self.driver.get(post_url)
            time.sleep(2)
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Author info
            author = {
                "name": self._clean_text(self._extract_text(soup, "span.share-posted-by__name")),
                "profile_url": self._extract_attribute(soup, "a.share-posted-by__profile-link", "href"),
                "headline": self._clean_text(self._extract_text(soup, "p.share-posted-by__headline"))
            }
            
            # Post content
            content = self._clean_text(self._extract_text(soup, "div.share-update-card__update-text"))
            
            # Post stats
            stats = {
                "likes": self._clean_text(self._extract_text(soup, "button.share-social-counts__count")),
                "comments": self._clean_text(self._extract_text(soup, "button.share-comments-button"))
            }
            
            # Post time
            post_time = self._clean_text(self._extract_text(soup, "span.share-posted-by__time"))
            
            return {
                "author": author,
                "content": content,
                "stats": stats,
                "post_time": post_time,
                "post_url": post_url,
                "scraped_at": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Post scraping error: {str(e)}")
            return {
                "error": "Post scraping failed",
                "details": str(e)
            }

    def save_data(self, data_type: str) -> dict:
        """Save data to JSON file"""
        if data_type not in self.current_data:
            return {"error": "No data to save"}
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{data_type}_{timestamp}.json"
            os.makedirs(self.output_folder, exist_ok=True)
            filepath = os.path.join(self.output_folder, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.current_data[data_type], f, indent=2, ensure_ascii=False)
            
            return {
                "success": True,
                "filepath": filepath,
                "items_saved": len(self.current_data[data_type])
            }
        except Exception as e:
            return {
                "error": "Save failed",
                "details": str(e)
            }

    def _extract_text(self, element, selector: str) -> str:
        """Helper to extract text from BeautifulSoup element"""
        try:
            found = element.select_one(selector)
            return found.get_text(strip=True) if found else ""
        except:
            return ""

    def _extract_attribute(self, element, selector: str, attribute: str) -> str:
        """Helper to extract attribute from BeautifulSoup element"""
        try:
            found = element.select_one(selector)
            return found.get(attribute, "") if found else ""
        except:
            return ""

    def _clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        if not text:
            return ""
        return ' '.join(text.split()).strip()

    def close(self):
        """Close browser session"""
        if self.driver:
            try:
                self.driver.quit()
                self.logged_in = False
            except:
                pass

class LinkedInScraperGUI:
    def __init__(self, root):
        self.root = root
        self.scraper = LinkedInScraper()
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main GUI interface"""
        self.root.title("LinkedIn Scraper Pro")
        self.root.geometry("1000x800")
        
        # Configure styles
        self.root.option_add("*Font", "Arial 10")
        self.root.option_add("*Button.Background", "#0077B5")
        self.root.option_add("*Button.Foreground", "white")
        self.root.option_add("*Button.activeBackground", "#005582")
        
        # Main container
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Login frame
        self.login_frame = Frame(self.main_frame, bd=2, relief="groove", padx=10, pady=10)
        self.login_frame.pack(fill="x", pady=(0, 10))
        
        Label(self.login_frame, text="LinkedIn Login", font=("Arial", 12, "bold")).pack(anchor="w")
        
        Label(self.login_frame, text="Email/Username:").pack(anchor="w")
        self.username_var = StringVar()
        Entry(self.login_frame, textvariable=self.username_var).pack(fill="x", pady=(0, 5))
        
        Label(self.login_frame, text="Password:").pack(anchor="w")
        self.password_var = StringVar()
        Entry(self.login_frame, textvariable=self.password_var, show="*").pack(fill="x", pady=(0, 10))
        
        Button(self.login_frame, text="Login", command=self.login).pack(fill="x")
        
        # Search frame (initially disabled)
        self.search_frame = Frame(self.main_frame, bd=2, relief="groove", padx=10, pady=10)
        self.search_frame.pack(fill="x", pady=(0, 10))
        
        Label(self.search_frame, text="LinkedIn Search", font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Search type selection
        self.search_type_var = StringVar(value="people")
        search_types = [("People", "people"), ("Companies", "companies"), 
                       ("Jobs", "jobs"), ("Posts", "posts")]
        
        search_type_frame = Frame(self.search_frame)
        search_type_frame.pack(fill="x", pady=(0, 10))
        
        for text, mode in search_types:
            btn = Button(search_type_frame, text=text, 
                        command=lambda m=mode: self.set_search_mode(m),
                        relief="sunken" if mode == "people" else "raised")
            btn.pack(side="left", expand=True, padx=2)
        
        # Search query
        Label(self.search_frame, text="Search Query:").pack(anchor="w", pady=(10, 0))
        self.search_var = StringVar()
        Entry(self.search_frame, textvariable=self.search_var).pack(fill="x", pady=(0, 5))
        
        # Location filter
        Label(self.search_frame, text="Location (optional):").pack(anchor="w")
        self.location_var = StringVar()
        Entry(self.search_frame, textvariable=self.location_var).pack(fill="x", pady=(0, 5))
        
        # Max results
        Label(self.search_frame, text="Max Results (10-100):").pack(anchor="w")
        self.max_results_var = StringVar(value="50")
        Entry(self.search_frame, textvariable=self.max_results_var).pack(fill="x", pady=(0, 10))
        
        Button(self.search_frame, text="Search", command=self.search).pack(fill="x")
        
        # Results frame
        self.results_frame = Frame(self.main_frame)
        self.results_frame.pack(fill="both", expand=True)
        
        # Text widget with scrollbar for results
        self.results_text = Text(self.results_frame, wrap="word", font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(self.results_frame, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        self.results_text.pack(side="left", fill="both", expand=True)
        
        # Status bar
        self.status_var = StringVar()
        self.status_var.set("Ready")
        status_bar = Label(self.root, textvariable=self.status_var, bd=1, relief="sunken", anchor="w")
        status_bar.pack(fill="x", padx=5, pady=(0, 5))
        
        # Disable search frame initially
        self.toggle_search_frame(False)
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def toggle_search_frame(self, enable: bool):
        """Enable or disable search controls"""
        state = "normal" if enable else "disabled"
        for child in self.search_frame.winfo_children():
            try:
                if not isinstance(child, Label):  # Keep labels enabled
                    child.configure(state=state)
            except:
                pass
    
    def login(self):
        """Handle login button click"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password")
            return
        
        self.status_var.set("Logging in...")
        self.root.update()
        
        if self.scraper.initialize_browser():
            if self.scraper.login_to_linkedin(username, password):
                messagebox.showinfo("Success", "Login successful!")
                self.status_var.set("Logged in - Ready to search")
                self.toggle_search_frame(True)
            else:
                messagebox.showerror("Error", "Login failed. Check credentials or try again later.")
                self.status_var.set("Login failed")
        else:
            messagebox.showerror("Error", "Failed to initialize browser. Check if ChromeDriver is installed.")
            self.status_var.set("Browser error")
    
    def set_search_mode(self, mode: str):
        """Set the search type"""
        self.search_type_var.set(mode)
        for child in self.search_frame.winfo_children()[1].winfo_children():  # Search type buttons frame
            if isinstance(child, Button):
                child.configure(relief="sunken" if child["text"].lower() == mode else "raised")
    
    def search(self):
        """Handle search button click"""
        if not self.scraper.logged_in:
            messagebox.showwarning("Not Logged In", "Please login first")
            return
        
        query = self.search_var.get().strip()
        search_type = self.search_type_var.get()
        location = self.location_var.get().strip() or None
        
        try:
            max_results = int(self.max_results_var.get())
            if max_results < 10 or max_results > 100:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Max results must be between 10 and 100")
            return
        
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search query")
            return
        
        self.status_var.set(f"Searching for '{query}'...")
        self.root.update()
        
        result = self.scraper.search_linkedin(query, search_type, location, max_results)
        
        if "error" in result:
            messagebox.showerror("Search Error", result["error"])
            self.status_var.set("Search failed")
        else:
            self.display_results(result["data"], search_type)
            stats = result.get("stats", {})
            location_text = f" in {location}" if location else ""
            self.status_var.set(f"Found {stats.get('total_results', 0)} {search_type} results{location_text}")
    
    def display_results(self, data, data_type):
        """Display results in text area"""
        self.results_text.delete(1.0, END)
        
        if not data:
            self.results_text.insert(END, "No results found")
            return
        
        self.results_text.insert(END, f"{data_type.upper()} RESULTS ({len(data)} items)\n{'='*50}\n\n")
        
        for i, item in enumerate(data, 1):
            self.results_text.insert(END, f"Result #{i}:\n")
            
            if data_type == "people":
                self.display_person_result(item)
            elif data_type == "companies":
                self.display_company_result(item)
            elif data_type == "jobs":
                self.display_job_result(item)
            elif data_type == "posts":
                self.display_post_result(item)
            
            self.results_text.insert(END, "\n" + "-"*50 + "\n\n")
        
        # Add save button
        Button(self.results_frame, text="Save Results to JSON", 
              command=lambda: self.save_data(data_type)).pack(pady=5)
    
    def display_person_result(self, item):
        """Display person search result"""
        self.results_text.insert(END, f"Name: {item.get('name', 'N/A')}\n")
        self.results_text.insert(END, f"Title: {item.get('title', 'N/A')}\n")
        self.results_text.insert(END, f"Location: {item.get('location', 'N/A')}\n")
        self.results_text.insert(END, f"Profile URL: {item.get('profile_url', 'N/A')}\n")
        
        details = item.get('profile_details', {})
        if details and not details.get('error'):
            self.results_text.insert(END, "\nDetailed Profile:\n")
            
            # Basic info
            basic = details.get('basic_info', {})
            self.results_text.insert(END, f"Headline: {basic.get('headline', 'N/A')}\n")
            self.results_text.insert(END, f"About: {basic.get('about', 'N/A')[:200]}...\n")
            
            # Contact info
            contact = details.get('contact_info', {})
            if contact:
                self.results_text.insert(END, f"\nContact Info:\n")
                self.results_text.insert(END, f"Email: {contact.get('email', 'N/A')}\n")
                self.results_text.insert(END, f"Phone: {contact.get('phone', 'N/A')}\n")
                if contact.get('websites'):
                    self.results_text.insert(END, "Websites:\n")
                    for site in contact['websites']:
                        self.results_text.insert(END, f"- {site.get('label', '')}: {site.get('url', '')}\n")
            
            # Experience
            if details.get('experience'):
                self.results_text.insert(END, "\nExperience:\n")
                for exp in details['experience'][:3]:  # Show first 3 experiences
                    self.results_text.insert(END, f"- {exp.get('title', '')} at {exp.get('company', '')} ({exp.get('duration', '')})\n")
            
            # Education
            if details.get('education'):
                self.results_text.insert(END, "\nEducation:\n")
                for edu in details['education'][:2]:  # Show first 2 educations
                    self.results_text.insert(END, f"- {edu.get('degree', '')} at {edu.get('school', '')} ({edu.get('duration', '')})\n")
            
            # Skills
            if details.get('skills'):
                self.results_text.insert(END, "\nTop Skills:\n")
                skills = ", ".join([s['name'] for s in details['skills'][:5]])  # Show top 5 skills
                self.results_text.insert(END, f"{skills}\n")
    
    def display_company_result(self, item):
        """Display company search result"""
        self.results_text.insert(END, f"Name: {item.get('name', 'N/A')}\n")
        self.results_text.insert(END, f"Industry: {item.get('industry', 'N/A')}\n")
        self.results_text.insert(END, f"Location: {item.get('location', 'N/A')}\n")
        self.results_text.insert(END, f"Profile URL: {item.get('profile_url', 'N/A')}\n")
        
        details = item.get('company_details', {})
        if details and not details.get('error'):
            self.results_text.insert(END, "\nDetailed Company Info:\n")
            
            # Basic info
            basic = details.get('basic_info', {})
            self.results_text.insert(END, f"Website: {basic.get('website', 'N/A')}\n")
            self.results_text.insert(END, f"Size: {basic.get('size', 'N/A')}\n")
            self.results_text.insert(END, f"Founded: {basic.get('founded', 'N/A')}\n")
            
            # About
            self.results_text.insert(END, f"\nAbout: {details.get('about', 'N/A')[:200]}...\n")
            
            # Specialties
            if details.get('specialties'):
                self.results_text.insert(END, "\nSpecialties:\n")
                self.results_text.insert(END, ", ".join(details['specialties'][:5]) + "\n")
            
            # Employees
            if details.get('employees_sample'):
                self.results_text.insert(END, "\nSample Employees:\n")
                for emp in details['employees_sample'][:3]:  # Show first 3 employees
                    self.results_text.insert(END, f"- {emp.get('name', '')}: {emp.get('title', '')}\n")
    
    def display_job_result(self, item):
        """Display job search result"""
        self.results_text.insert(END, f"Title: {item.get('title', 'N/A')}\n")
        self.results_text.insert(END, f"Company: {item.get('company', 'N/A')}\n")
        self.results_text.insert(END, f"Location: {item.get('location', 'N/A')}\n")
        self.results_text.insert(END, f"Posted: {item.get('time', 'N/A')}\n")
        self.results_text.insert(END, f"Job URL: {item.get('job_url', 'N/A')}\n")
        
        details = item.get('job_details', {})
        if details and not details.get('error'):
            self.results_text.insert(END, "\nDetailed Job Info:\n")
            
            self.results_text.insert(END, f"Applicants: {details.get('applicants', 'N/A')}\n")
            
            # Criteria
            if details.get('criteria'):
                self.results_text.insert(END, "\nJob Criteria:\n")
                for key, value in details['criteria'].items():
                    self.results_text.insert(END, f"- {key.replace('_', ' ').title()}: {value}\n")
            
            # Description
            self.results_text.insert(END, f"\nJob Description:\n{details.get('description', 'N/A')[:300]}...\n")
    
    def display_post_result(self, item):
        """Display post search result"""
        self.results_text.insert(END, f"Author: {item.get('author', 'N/A')}\n")
        self.results_text.insert(END, f"Content: {item.get('content', 'N/A')[:100]}...\n")
        self.results_text.insert(END, f"Time: {item.get('time', 'N/A')}\n")
        self.results_text.insert(END, f"Post URL: {item.get('post_url', 'N/A')}\n")
        
        details = item.get('post_details', {})
        if details and not details.get('error'):
            self.results_text.insert(END, "\nDetailed Post Info:\n")
            
            # Author info
            if details.get('author'):
                author = details['author']
                self.results_text.insert(END, f"Author Profile: {author.get('profile_url', 'N/A')}\n")
                self.results_text.insert(END, f"Author Headline: {author.get('headline', 'N/A')}\n")
            
            # Stats
            if details.get('stats'):
                stats = details['stats']
                self.results_text.insert(END, f"Likes: {stats.get('likes', 'N/A')}\n")
                self.results_text.insert(END, f"Comments: {stats.get('comments', 'N/A')}\n")
            
            # Content
            self.results_text.insert(END, f"\nFull Content:\n{details.get('content', 'N/A')[:500]}...\n")
    
    def save_data(self, data_type):
        """Save the current results"""
        result = self.scraper.save_data(data_type)
        if "error" in result:
            messagebox.showerror("Save Error", result["error"])
        else:
            messagebox.showinfo("Success", f"Data saved to:\n{result['filepath']}")
            webbrowser.open(os.path.dirname(result['filepath']))
    
    def on_closing(self):
        """Handle window closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.scraper.close()
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = LinkedInScraperGUI(root)
    root.mainloop()