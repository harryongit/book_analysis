# src/scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from typing import List, Dict
import logging

class BookScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a webpage"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            self.logger.error(f"Error fetching page {url}: {e}")
            return None

    def scrape_book_data(self, num_pages: int) -> List[Dict]:
        """Scrape book data from multiple pages"""
        books_data = []
        
        for page in range(1, num_pages + 1):
            self.logger.info(f"Scraping page {page}")
            url = f"{self.base_url}/page/{page}"
            soup = self.get_page(url)
            
            if soup:
                books = soup.find_all('div', class_='book-info')
                for book in books:
                    book_data = {
                        'title': book.find('h2').text.strip(),
                        'author': book.find('span', class_='author').text.strip(),
                        'rating': float(book.find('span', class_='rating').text),
                        'reviews': int(book.find('span', class_='reviews').text.replace(',', '')),
                        'genres': [g.text for g in book.find_all('span', class_='genre')]
                    }
                    books_data.append(book_data)
            
            time.sleep(1)  # Be nice to the server
        
        return books_data

    def save_to_csv(self, data: List[Dict], filename: str):
        """Save scraped data to CSV"""
        df = pd.DataFrame(data)
        df.to_csv(f"data/raw/{filename}", index=False)
        self.logger.info(f"Data saved to {filename}")
