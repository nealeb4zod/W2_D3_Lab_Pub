import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        drink_1 = Drink("beer", 5.00)
        drink_2 = Drink("vodka", 3.00)
        drink_3 = Drink("cocktail", 7.00)
        list_of_drinks = [drink_1,drink_2, drink_3]
        self.pub = Pub("The Prancing Pony", 100.00, list_of_drinks)

    def test_pub_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_drinks_number(self):
        self.assertEqual(3 , len(self.pub.drinks))

    
    def test_add_money_to_till(self):
        drink_1 = Drink("beer", 5.00)
        self.pub.add_money_to_till(self.pub, drink_1)
        self.assertEqual(105.00, self.pub.till)