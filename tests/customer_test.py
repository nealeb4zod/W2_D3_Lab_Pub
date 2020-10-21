import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer_1 = Customer("Mark", 100.00)
        self.customer_2 = Customer("Ed", 6.00)
        

    def test_customer_name(self):
        self.assertEqual("Mark", self.customer_1.name)

    def test_customer_wallet(self):
        self.assertEqual(100.00, self.customer_1.wallet)

    def test_customer_can_afford_drink(self):
        drink_1 = Drink("Beer", 5.00)
        
        self.assertEqual(True, self.customer_1.customer_can_afford_drink(self.customer_1, drink_1))

    def test_customer_cannot_afford_drink(self):
        drink_1 = Drink("cocktail", 7.00)
        self.assertEqual(False, self.customer_2.customer_can_afford_drink(self.customer_2, drink_1))

    def test_remove_money_from_wallet(self):
        drink_1 = Drink("Beer", 5.00)
        self.customer_1.remove_money_from_wallet(self.customer_1, drink_1)
        self.assertEqual(95.00, self.customer_1.wallet)

    def test_customer_can_buy_drink(self):
        drink_1 = Drink("beer", 5.00)
        drink_2 = Drink("vodka", 3.00)
        drink_3 = Drink("cocktail", 7.00)
        list_of_drinks = [drink_1,drink_2, drink_3]
        pub = Pub("The Prancing Pony", 100.00, list_of_drinks)
        self.customer_1.customer_can_buy_drink(self.customer_1, drink_1, pub)
        self.assertEqual(95.00, self.customer_1.wallet)
        self.assertEqual(105.00, pub.till)
        # check if customer can afford it drink
        #     reduce money from wallet
        #     add money to till
        