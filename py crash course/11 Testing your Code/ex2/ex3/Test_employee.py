

# Test employee class ex3

import unittest
from Employee import Employee 

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
            Create an employee class to test with
        """
        self.fname = "John"
        self.lname = "Doyle"
        self.salary = 60000
        self.John = Employee("John","Doyle",60000)
    
    def test_give_raise(self):
        """Lets give John the default raise"""
        self.John.give_raise()
        self.assertEqual(self.John.salary,self.salary+5000)
    
    def test_give_custom_raise(self):
        """Give John a raise of 20000"""
        JohnsRaise = 20000
        self.John.give_raise(JohnsRaise)
        self.assertEqual(self.John.salary,self.salary+JohnsRaise)




unittest.main()

