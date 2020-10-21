import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):

        drink_1 = Drink("beer", 5.00, 2, 120)
        drink_2 = Drink("vodka", 3.00, 3, 30)
        drink_3 = Drink("cocktail", 7.00, 8, 25)
        list_of_drinks = [drink_1, drink_2, drink_3]
        self.pub = Pub("The Prancing Pony", 100.00, list_of_drinks)

    def test_pub_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_drink_availability(self):
        drink_1 = Drink("beer", 5.00, 2, 1)
        self.assertEqual(True, self.pub.drink_available(drink_1))

    def test_pub_drinks_number(self):
        self.assertEqual(3, len(self.pub.drinks))

    def test_drunkenness(self):
        customer_1 = Customer("Mark", 100.00, 33)
        drink_1 = Drink("beer", 5.00, 6, 1)
        customer_1.make_drunk(drink_1)
        customer_1.make_drunk(drink_1)
        self.assertEqual(True, self.pub.check_drunkenness(customer_1))

    def test_add_money_to_till(self):
        drink_1 = Drink("beer", 5.00, 2, 1)
        self.pub.add_money_to_till(drink_1)
        self.assertEqual(105.00, self.pub.till)

    def test_stock_count(self):
        self.assertEqual(865, self.pub.stock_count())

    def test_remove_item_from_stock(self):
        drink_1 = Drink("beer", 5.00, 2, 1)
        self.pub.remove_item_from_stock(drink_1)
        self.assertEqual(119, self.pub.check_quantity(drink_1))
