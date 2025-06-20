import requests
from bs4 import BeautifulSoup

# Step 1: Get the website content
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find quotes and authors
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Step 4: Print them
for i in range(len(quotes)):
    print(f"Quote: {quotes[i].text}")
    print(f"Author: {authors[i].text}")
    print("-" * 30)
