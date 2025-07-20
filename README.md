# Book Scraper with Streamlit Visualization

A web scraping project to extract book data (title, price, rating) from [Books to Scrape](https://books.toscrape.com/) using Scrapy, visualized in a Streamlit app, and hosted on Streamlit Cloud.

## Features
- Scrapes book titles, prices, and ratings.
- Saves data to `books.csv`.
- Streamlit app visualizes:
  - Raw data table
  - Price distribution histogram
  - Rating counts bar chart
  - Summary statistics
- Hosted on Streamlit Cloud.

## Prerequisites
- Python 3.x
- Visual Studio Code
- Git
- Streamlit Cloud account
- Libraries: `scrapy`, `pandas`, `streamlit`, `plotly`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/book-scraper.git
   cd book-scraper