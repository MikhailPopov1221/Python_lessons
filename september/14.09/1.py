import requests
from bs4 import BeautifulSoup


base_url = "https://quotes.toscrape.com"
response = requests.get(base_url)

soup = BeautifulSoup(response.text, "lxml")
quotes = soup.find_all("div", class_ = "quote")

data = []

for quote in quotes:
    quote_text = quote.find("span", class_ = "text").get_text(strip=True)
    quote_author = quote.find("small", class_ = "author").get_text(strip=True)
    
    d = {"author": quote_author, "quote": quote_text}
    data.append(d)
    
next_btn = soup.find("li", class_ = "next")
if next_btn:
    url = base_url + next_btn.a["href"]
    print(url)


# print(next_btn.prettify())