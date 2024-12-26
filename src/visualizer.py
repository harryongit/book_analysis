# src/visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Dict, Any

class BookVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        plt.style.use('seaborn')

    def create_rating_distribution(self):
        """Create rating distribution plot"""
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x='rating', bins=20)
        plt.title('Distribution of Book Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.savefig('data/visualizations/rating_distribution.png')
        plt.close()

    def create_genre_analysis(self, genre_stats: pd.DataFrame):
        """Create genre analysis visualizations"""
        plt.figure(figsize=(12, 6))
        sns.barplot(data=genre_stats.head(10), x=genre_stats.index, y='avg_rating')
        plt.title('Average Rating by Genre (Top 10)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('data/visualizations/genre_ratings.png')
        plt.close()

    def create_review_vs_rating_plot(self):
        """Create scatter plot of reviews vs ratings"""
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x='review_count_log', y='rating', alpha=0.5)
        plt.title('Relationship Between Reviews and Ratings')
        plt.xlabel('Log Number of Reviews')
        plt.ylabel('Rating')
        plt.savefig('data/visualizations/reviews_vs_ratings.png')
        plt.close()
