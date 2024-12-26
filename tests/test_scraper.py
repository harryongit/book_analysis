# tests/test_scraper.py
import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import sys
sys.path.append('..')
from src.scraper import BookScraper

class TestBookScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = BookScraper('https://example-book-site.com')
        
    @patch('requests.get')
    def test_get_page(self, mock_get):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.text = '<html><body><div class="book-info"></div></body></html>'
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        result = self.scraper.get_page('https://example.com')
        self.assertIsInstance(result, BeautifulSoup)
        
    @patch('requests.get')
    def test_get_page_error(self, mock_get):
        # Mock failed response
        mock_get.side_effect = requests.RequestException()
        
        result = self.scraper.get_page('https://example.com')
        self.assertIsNone(result)
        
    @patch('src.scraper.BookScraper.get_page')
    def test_scrape_book_data(self, mock_get_page):
        # Mock HTML content
        mock_html = '''
        <div class="book-info">
            <h2>Test Book</h2>
            <span class="author">Test Author</span>
            <span class="rating">4.5</span>
            <span class="reviews">1,000</span>
            <span class="genre">Fiction</span>
            <span class="genre">Mystery</span>
        </div>
        '''
        mock_get_page.return_value = BeautifulSoup(mock_html, 'html.parser')
        
        result = self.scraper.scrape_book_data(num_pages=1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], 'Test Book')
        self.assertEqual(result[0]['rating'], 4.5)
