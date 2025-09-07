from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
login = os.getenv("LOGIN", "username")
password = os.getenv("PASSWORD", "password")


print(api_key)
print(login)
print(password)