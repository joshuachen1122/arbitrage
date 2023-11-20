import requests
from bs4 import BeautifulSoup
from scraper import parse_html_table

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None

def main():
    url = 'https://www.oddstrader.com/nba/?g=game&m=money'
    html = get_html(url)
    
    if not html:
        print("Failed to retrieve HTML content. Exiting.")
        return

    parse_html_table(html)

if __name__ == "__main__":
    main()