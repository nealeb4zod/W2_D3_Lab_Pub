import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("beer", 5.00)