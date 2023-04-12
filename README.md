# FLORIDA-MAN

Using the Google Custom Search JSON API to retrieve "Florida Man" stories from news headlines on this day in previous years.

## Quickstart

Before beginning, create a project on Google Cloud Platform and enable the Custom Search JSON API. This project is built on Python 3.8, but should work on all 3.X versions.
1. Create a `.env` file under `/src` containing GOOGLE_SEARCH_API_KEY and GOOGLE_SEARCH_ENGINE_ID.
2. `pip install -r requirements.txt`
3. `python main.py`

## Notes

This prefers the Search API over News API for the Search API's equivalent free tier and more flexible pricing model.