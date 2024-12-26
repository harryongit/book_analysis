# src/data_processor.py
import pandas as pd
import numpy as np
from typing import List
import logging

class DataProcessor:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def load_data(self, filename: str) -> pd.DataFrame:
        """Load data from CSV file"""
        return pd.read_csv(f"data/raw/{filename}")

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and preprocess the data"""
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.dropna(subset=['title', 'author', 'rating'])
        
        # Convert genres from string to list if needed
        if isinstance(df['genres'].iloc[0], str):
            df['genres'] = df['genres'].apply(eval)
        
        # Create additional features
        df['review_count_log'] = np.log1p(df['reviews'])
        df['is_highly_rated'] = df['rating'] >= 4.0
        
        return df

    def process_genres(self, df: pd.DataFrame) -> pd.DataFrame:
        """Process and explode genres into separate rows"""
        return df.explode('genres').reset_index(drop=True)

    def save_processed_data(self, df: pd.DataFrame, filename: str):
        """Save processed data to CSV"""
        df.to_csv(f"data/processed/{filename}", index=False)
        self.logger.info(f"Processed data saved to {filename}")
