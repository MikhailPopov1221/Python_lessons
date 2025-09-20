import requests
from bs4 import BeautifulSoup
import time
import xlsxwriter

data = []

base_url = "https://quotes.toscrape.com"
url = base_url

while url:
    time.sleep(2)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = soup.find_all("div", class_ = "quote")


    for quote in quotes:
        quote_text = quote.find("span", class_ = "text").get_text(strip=True)
        quote_author = quote.find("small", class_ = "author").get_text(strip=True)
        
        d = {"author": quote_author, "quote": quote_text}
        data.append(d)
        
    next_btn = soup.find("li", class_ = "next")
    if next_btn:
        url = base_url + next_btn.a["href"]
        print(url)
    else:
        url = None

print("--------------------------------------------")
print(f"Парсинг завершен, найдено {len(data)} цитат")


workbook = xlsxwriter.Workbook("quotes.xlsx")
worksheet = workbook.add_worksheet("Quotes")

# Вариант №1 - простой
header_format = workbook.add_format({
        "bold": True,
        "border": 1,
        "align": "center",
        "valign": "vcenter"
})

text_format = workbook.add_format({
    "border": 1,
    "align": "left",
    "text_wrap": True
})

worksheet.set_column(0, 0, 25)
worksheet.set_column(1, 1, 300)
worksheet.set_row(0, 30)

worksheet.write(0, 0, "Author", header_format)
worksheet.write(0, 1, "Quote", header_format)

for row, elem in enumerate(data, start=1):
    worksheet.write(row,0, elem["author"], text_format)
    worksheet.write(row,1, elem["quote"], text_format)

workbook.close()

print("Файл exel успешно создан")