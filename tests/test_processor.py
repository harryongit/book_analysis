# tests/test_processor.py
import unittest
import pandas as pd
import numpy as np
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()
        
        # Create sample data
        self.sample_data = pd.DataFrame({
            'title': ['Book1', 'Book2', 'Book3'],
            'author': ['Author1', 'Author2', 'Author3'],
            'rating': [4.5, 3.8, None],
            'reviews': [100, 200, 300],
            'genres': [['Fiction'], ['Mystery', 'Thriller'], ['Fiction']]
        })
        
    def test_clean_data(self):
        cleaned_df = self.processor.clean_data(self.sample_data)
        
        # Check if NaN values are removed
        self.assertEqual(len(cleaned_df), 2)
        
        # Check if new features are created
        self.assertTrue('review_count_log' in cleaned_df.columns)
        self.assertTrue('is_highly_rated' in cleaned_df.columns)
        
    def test_process_genres(self):
        processed_df = self.processor.process_genres(self.sample_data)
        
        # Check if genres are properly exploded
        self.assertTrue(len(processed_df) > len(self.sample_data))
        self.assertTrue(isinstance(processed_df['genres'].iloc[0], str))
