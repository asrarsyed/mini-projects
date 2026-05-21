import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

HEADERS = {"User-Agent": "Mozilla/5.0"}

books = []

for page in range(1, 51):
    url = BASE_URL.format(page)

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Failed page {page}: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select("article.product_pod")

    for article in articles:
        title = article.select_one("img")["alt"]  # type: ignore

        rating = article.select_one("p.star-rating")["class"][1]  # type: ignore

        price_text = article.select_one(".price_color").text  # type: ignore
        price = float("".join(c for c in price_text if c.isdigit() or c == "."))

        books.append({"Title": title, "Rating": rating, "Price": price})

df = pd.DataFrame(books)
df.to_csv("books.csv", index=False)
