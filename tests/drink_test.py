import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("beer", 5.00)

    def test_drink_name(self):
        self.assertEqual("beer", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(5.00, self.drink.price)