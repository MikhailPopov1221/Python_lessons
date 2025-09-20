import requests
import time


base_url = "https://quotes.toscrape.com/api/quotes?page="

url = base_url + "1"

while url:
    time.sleep(2)
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Ошибка получения данных")
        break
    
    data = response.json()
    
    quotes = data["quotes"]
    
    for quote in quotes:
        print()
        print(quote.get("text", ""))
        print(quote["author"]["name"])
        print(" - ".join(quote["tags"]))
        print()
    

    next = data.get("has_next", False)
    next_page = data.get("page", False)
    
    if next and next_page:
        url = base_url + str(next_page + 1)
    else:
        url = None
        
    print(f"Перходим к странице №{next_page}...")
