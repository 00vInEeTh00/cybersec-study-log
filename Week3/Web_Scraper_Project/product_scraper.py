# oxylabs products scraping.

import requests
from bs4 import BeautifulSoup

url = "https://sandbox.oxylabs.io/products"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
product_cards = soup.find_all("div",class_="product-card")

for card in product_cards:
    title = card.find("h4",class_="title").text.strip()
    category = card.find("p",class_="category").text.strip()
    description = card.find("p",class_="description").text.strip()
    price = card.find("div",class_="price-wrapper").text.strip()
    stock = card.find("p",class_="in-stock")
    print("---------------------------------------------------")
    print("Titile     : ",title)
    print(" ")
    print("Category   : ",category)
    print(" ")
    print("Descripion : ",description)
    print(" ")
    print("Price      : ",price)
    print(" ")
    print("Stock      : ",stock)
    print("\n")

