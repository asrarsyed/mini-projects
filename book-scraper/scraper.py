import requests
from bs4 import BeautifulSoup
import pandas as pd

# Book list
books = []

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    response = response.content

    soup = BeautifulSoup(response, "html.parser")

    # Find the first ol
    orderlst = soup.find("ol")

    # Find all articles
    articles = orderlst.find_all("article", class_="product_pod")  # type:ignore

    # Iterate through datapoints in every article
    for article in articles:
        # title
        title = article.find("img").get("alt")  # type:ignore

        # rating
        rating = article.find("p")["class"][1]  # type:ignore

        # price
        price = float(article.find("p", class_="price_color").text[1:])  # type:ignore

        # Append data as dictionary
        books.append({"Title": title, "Rating": rating, "Price": price})

# Create DataFrame
df = pd.DataFrame(books)

# Save to CSV
df.to_csv("books.csv", index=False)
