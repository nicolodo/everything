
import unittest
from city_functions import city_country

# we are testing the city_country function

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country() function"""

    def Test_city_country(self):
        compareName = "London, England"
        city = "London"
        country = "England"
        combinedName = city_country(city,country)

        print(combinedName,compareName)

        self.assertEqual(combinedName,compareName)

unittest.main()


    
