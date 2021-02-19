import unittest
from ..breweries import Breweries
import os
from dotenv import load_dotenv

class TestBreweriesMethods(unittest.TestCase):
    
    def setUp(self):
        load_dotenv()
        self.breweries = Breweries(os.getenv('BREWERY_DB_API_KEY'))

    def test_get_random_brewery(self):
        self.assertEqual(self.breweries.get_random_brewery(), 'SUCCESS')

if __name__ == '__main__':
    unittest.main()
