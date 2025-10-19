import requests
from bs4 import BeautifulSoup

def fetch_competitor_data(query):
    urls = [
        f"https://www.flipkart.com/search?q={query}",
        f"https://www.amazon.in/s?k={query}"
    ]
    data = []
    for url in urls:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.find_all("div", class_="product-title")
        prices = soup.find_all("div", class_="product-price")
        for t, p in zip(titles, prices):
            data.append(f"{t.text.strip()} - {p.text.strip()}")
    return data
