# Book Data Analysis Project

This project scrapes book data from a book review website and performs comprehensive analysis on ratings, reviews, and genres.

## Features
- Web scraping with rate limiting and error handling
- Data cleaning and preprocessing
- Statistical analysis of books, authors, and genres
- Data visualization
- Comprehensive test suite

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main analysis:
   ```bash
   python main.py
   ```
2. View visualizations in the `data/visualizations` directory
3. Explore the Jupyter notebook in `notebooks/analysis.ipynb`

## Project Structure
```
book_analysis/
│
├── src/                 # Source code
├── data/               # Data directory
├── notebooks/          # Jupyter notebooks
├── tests/             # Unit tests
├── requirements.txt    # Dependencies
└── README.md          # Documentation
```

## Testing
Run tests using:
```bash
python -m unittest discover tests
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
MIT License
