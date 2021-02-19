import os
from dotenv import load_dotenv

class Breweries:
    def __init__(self, key):
        self.key = key


load_dotenv()
x = os.getenv('BREWERY_DB_API_KEY')
print(x)
