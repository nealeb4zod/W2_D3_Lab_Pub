import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Mark", 100.00, 33)
        self.customer_2 = Customer("Ed", 6.00, 16)
        self.drink_1 = Drink("Beer", 5.00, 2, 1)
        self.drink_2 = Drink("bottle of vodka", 30.00, 10, 1)

    def test_customer_name(self):
        self.assertEqual("Mark", self.customer_1.name)

    def test_customer_wallet(self):
        self.assertEqual(100.00, self.customer_1.wallet)

    def test_customer_age(self):
        self.assertEqual(33, self.customer_1.age)

    def test_customer_drunkenness(self):
        self.assertEqual(0, self.customer_1.drunkenness)

    def test_make_drunk(self):
        self.customer_1.make_drunk(self.drink_1)
        self.assertEqual(2, self.customer_1.drunkenness)

    def test_make_sober(self):
        food_1 = Food("Steak", 11.99, 8)
        self.customer_1.make_drunk(self.drink_2)
        self.customer_1.make_sober(food_1)
        self.assertEqual(2, self.customer_1.drunkenness)

    def test_customer_can_afford_drink(self):
        self.assertEqual(
            True,
            self.customer_1.customer_can_afford_item(self.drink_1),
        )

    def test_customer_can_afford_food(self):
        food_1 = Food("Chips", 1.50, 2)
        self.assertEqual(True, self.customer_1.customer_can_afford_item(food_1))

    def test_customer_cannot_afford_food(self):
        food_1 = Food("Chips", 6.50, 2)
        self.assertEqual(False, self.customer_2.customer_can_afford_item(food_1))

    def test_customer_cannot_afford_drink(self):
        drink_1 = Drink("cocktail", 7.00, 3, 1)
        self.assertEqual(False, self.customer_2.customer_can_afford_item(drink_1))

    def test_remove_money_from_wallet(self):
        self.customer_1.remove_money_from_wallet(self.drink_1)
        self.assertEqual(95.00, self.customer_1.wallet)

    def test_age_challenge(self):
        customer_2 = Customer("Ed", 6.00, 16)
        self.assertEqual(False, self.customer_2.age_challenge())

    def test_customer_can_buy_drink(self):
        drink_2 = Drink("vodka", 3.00, 1, 1)
        drink_3 = Drink("cocktail", 7.00, 3, 1)
        list_of_drinks = [self.drink_1, drink_2, drink_3]
        pub = Pub("The Prancing Pony", 100.00, list_of_drinks)
        self.customer_1.customer_can_buy_drink(self.drink_1, pub)
        self.assertEqual(95.00, self.customer_1.wallet)
        self.assertEqual(105.00, pub.till)