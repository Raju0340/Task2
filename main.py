import requests
from bs4 import BeautifulSoup
websites = [
     "https://und.edu/",
    "https://www.washington.edu/",
    "https://www.stanford.edu/"
    
]

def search_in_content(query, content_dict):
    """Searches for a query in the scraped content and returns matching results."""
    matches = []
    for url, content in content_dict.items():
        if query.lower() in content.lower():
            matches.append((url, content))
    return matches
def fetch_website_content(url):
     """Fetches and returns the text content of a website."""
     try:
        response= requests.get(url, timeout=10)
        response.raise_for_status()
        soup =BeautifulSoup (response.text, 'html.parser')
        return soup.get_text(separator='', strip=True)
     except requests.exceptions.SSLError as ssl_err:
       print(f" An SSL error occurred: {ssl_err}")
     except requests.exceptions.RequestException as req_err:
       print(f"Request error occurred: {req_err}")
     except Exception as e:
      print(f"An error has occurred: {e}")

scraped_content = {}
for w in websites:
    content= fetch_website_content(w)
    if content:
        print(f"Successfully scraped content from the {w}")
        scraped_content[w] =content
query_input= input("Enter your query: ")
search_results =search_in_content(query_input, scraped_content)
if search_results:
    print("\n Results found:")
    for url, content in search_results:
        print(f"\nFrom {url}:\n{content[:200]}...")
else:
    print("No search results found for your query.")
