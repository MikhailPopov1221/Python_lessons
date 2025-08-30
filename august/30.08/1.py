import requests


url = "https://www.google.com"

response = requests.get(url)

print(f"Код ответа: {response.status_code}")

# print("Заголовки: ")
# for key, value in response.headers.items():
#     print(f"{key}: {value}")

print(f"Тело страницы: {response.text}")

with open("google.html", "w", encoding="utf-8") as fl:
    fl.write(response.text)