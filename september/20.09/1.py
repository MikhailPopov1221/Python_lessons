import requests


url = "https://quotes.toscrape.com/scroll"
response = requests.get(url)
print(response.text)