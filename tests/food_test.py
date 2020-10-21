import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food_1 = Food("Chips", 1.50, 2)
        self.food_2 = Food("Steak", 11.99, 8)
    
    def test_food_name(self):
        self.assertEqual("Chips", self.food_1.name)
    
    def test_food_price(self):
        self.assertEqual(1.50, self.food_1.price)

    def test_food_rejuvination_level(self):
        self.assertEqual(8, self.food_2.rejuvenation_level)