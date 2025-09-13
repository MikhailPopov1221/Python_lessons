import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"
response = requests.get(url)

# print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
# print(soup.text)
# print(soup.prettify())

quote = soup.find("div", class_ = "quote")
# print(quote.text)
# print(quote.prettify())

quote_text = quote.find("span", class_ = "text").get_text(strip=True)
quote_author = quote.find("small", class_ = "author").get_text(strip=True)
print(quote_text)
print(quote_author)

