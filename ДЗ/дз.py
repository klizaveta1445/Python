import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = ", ".join(tag.text for tag in quote.find_all("a", class_="tag"))

    quotes_data.append({
        "quote": text,
        "author": author,
        "tags": tags
    })

df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False, encoding="utf-8")

print("Первые строки датасета:")
print(df.head(), "\n")

print("Размер датасета:")
print(df.shape, "\n")

print("Количество цитат по авторам:")
print(df["author"].value_counts())
