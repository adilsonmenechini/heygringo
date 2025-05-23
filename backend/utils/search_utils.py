# backend/utils/search_utils.py
from duckduckgo_search import DDGS
from utils.logger import error, info # Assuming your logger setup

# Optional:
# import requests # If you need to fetch content from URLs directly
# from bs4 import BeautifulSoup # If you need to parse HTML from URLs

def perform_search(query: str, max_results: int = 3) -> list[dict] | None:
    info(f"Performing DuckDuckGo search for: {query}")
    try:
        with DDGS() as ddgs:
            results_generator = ddgs.text(query, max_results=max_results)
            # ddgs.text returns a generator of dictionaries like:
            # {'title': '...', 'href': '...', 'body': '...'}
            
            # Convert generator to list to check if it's empty
            results = list(results_generator)

            if not results:
                info(f"No search results found for: {query}")
                return []

            processed_results = []
            for result in results:
                processed_results.append({
                    "title": result.get('title', 'N/A'),
                    "snippet": result.get('body', 'N/A'),
                    "url": result.get('href', '#')
                })
            info(f"Found {len(processed_results)} results for query: {query}")
            return processed_results

    except Exception as e:
        error(f"Error during DuckDuckGo search for '{query}': {e}")
        return None
