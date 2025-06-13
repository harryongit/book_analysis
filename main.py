# main.py
def main():
    # Initialize scraper
    scraper = BookScraper('https://example-book-site.com')


    # Scrape data
    books_data = scraper.scrape_book_data(num_pages=10)
    scraper.save_to_csv(books_data, 'raw_books.csv')
    
    # Process data
    processor = DataProcessor()
    df = processor.load_data('raw_books.csv')
    df_clean = processor.clean_data(df)
    df_processed = processor.process_genres(df_clean)
    processor.save_processed_data(df_processed, 'processed_books.csv')
    
    # Analyze data
    analyzer = BookAnalyzer(df_processed)
    basic_stats = analyzer.calculate_basic_stats()
    genre_stats = analyzer.analyze_genres()
    author_stats = analyzer.author_analysis()
    correlations = analyzer.correlation_analysis()
    
    # Create visualizations
    visualizer = BookVisualizer(df_processed)
    visualizer.create_rating_distribution()
    visualizer.create_genre_analysis(genre_stats)
    visualizer.create_review_vs_rating_plot()

if __name__ == "__main__":
    main()
