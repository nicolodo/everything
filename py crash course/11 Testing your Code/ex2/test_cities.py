
import unittest
from city_functions import city_country

# we are testing the city_country function

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country() function"""

    def test_city_country(self):
        compareName = "London, England"
        city = "London"
        country = "England"
        combinedName = city_country(city,country,5000)
        print(combinedName)

        print(combinedName,compareName)

        self.assertEqual(combinedName,compareName)
    
    def test_city_country_population(self):
        compareName = "London, England - 10000000"
        city = "London"
        country = "England"
        population = "10000000"
        combinedName = city_country(city,country,population)
        print(combinedName)

        print(combinedName +' : '+ compareName)

        self.assertEqual(combinedName,compareName)



unittest.main()


    