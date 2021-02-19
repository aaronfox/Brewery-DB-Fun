from brewery_package.breweries import Breweries
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    breweries = Breweries(os.getenv('BREWERY_DB_API_KEY'))
    breweries.print_test()
    breweries.get_random_brewery()

if __name__ == "__main__":
    main()
    