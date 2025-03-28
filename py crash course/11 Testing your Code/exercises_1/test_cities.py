
# ex1 importing city functions 
# and seeing if it works

import unittest
from city_functions import city_country

class cityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like Vatican City, Vatican City work?"""
        city = city_country('vatican city','vatican city')
        print(f"The city is {city}")
        self.assertEqual('vatican city, vatican city','vatican city, vatican city')




