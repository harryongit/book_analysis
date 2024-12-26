# src/analyzer.py
import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, Any
import logging


class BookAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def calculate_basic_stats(self) -> Dict[str, Any]:
        """Calculate basic statistics about the books"""
        stats = {
            'total_books': len(self.df),
            'average_rating': self.df['rating'].mean(),
            'median_rating': self.df['rating'].median(),
            'total_reviews': self.df['reviews'].sum(),
            'unique_authors': self.df['author'].nunique(),
            'top_rated_book': self.df.loc[self.df['rating'].idxmax(), 'title'],
            'most_reviewed_book': self.df.loc[self.df['reviews'].idxmax(), 'title']
        }
        return stats

    def analyze_genres(self) -> pd.DataFrame:
        """Analyze genre statistics"""
        genre_stats = self.df.groupby('genres').agg({
            'rating': ['count', 'mean', 'std'],
            'reviews': 'sum'
        }).round(2)
        
        genre_stats.columns = ['book_count', 'avg_rating', 'rating_std', 'total_reviews']
        return genre_stats.sort_values('book_count', ascending=False)

    def author_analysis(self) -> pd.DataFrame:
        """Analyze author statistics"""
        author_stats = self.df.groupby('author').agg({
            'title': 'count',
            'rating': 'mean',
            'reviews': 'sum'
        }).round(2)
        
        author_stats.columns = ['book_count', 'avg_rating', 'total_reviews']
        return author_stats.sort_values('book_count', ascending=False)

    def correlation_analysis(self) -> pd.DataFrame:
        """Analyze correlations between numerical variables"""
        numerical_cols = ['rating', 'reviews', 'review_count_log']
        return self.df[numerical_cols].corr().round(3)
