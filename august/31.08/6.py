import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import json


API_KEY = "4f9b202aad6f410fb9064551250802"

URL = "http://api.weatherapi.com/v1/current.json"

params = {
    "key" : API_KEY,
    "q": "55.77 38.65",
    "aqi": "no"
}

with sqlite3.connect("weather.db") as connection:
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        last_updated TEXT
        )
    ''')
    connection.commit()


def write_to_db(dct: dict):
    with sqlite3.connect("weather.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO weather (city, temperature, last_updated)
            VALUES (?,?,?)
        ''', (dct["name"], dct["temp_c"], dct["last_updated"])
        )
        connection.commit()


def get_current_weather():
    response = requests.get(URL, params)
    if response.status_code == 200:
        return response.json()
    return None

def get_information(data):
    return {
        "name" : data["location"]["name"],
        "temp_c": data["current"]["temp_c"],
        "last_updated": data["current"]["last_updated"]
    }
    
def launch():
    print("Начало загрузки")
    data = get_current_weather()
    data = get_information(data)
    write_to_db(data)
    print("Данные успешно загружены")
    
scheduler = BackgroundScheduler()
scheduler.add_job(launch, "interval", seconds=10)
scheduler.start()

while True:
    pass


# print()
# # if data:
# #     print(json.dumps(data, indent=4, ensure_ascii=False))

# write_to_db(get_information(data))