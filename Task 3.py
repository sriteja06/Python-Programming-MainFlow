import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extract all headings (h1 to h3)
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            print(heading.name + ': ' + heading.get_text(strip=True))
        
        # Example: Extract all hyperlinks
        for link in soup.find_all('a', href=True):
            print('Link:', link['href'])
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    scrape_website(url)