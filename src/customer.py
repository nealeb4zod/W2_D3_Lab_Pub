class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def make_drunk(self, drink):
        self.drunkenness += drink.alcohol_level

    def make_sober(self, food):
        self.drunkenness -= food.rejuvenation_level

    def customer_can_afford_item(self, item):
        if self.wallet >= item.price:
            return True
        else:
            return False

    def age_challenge(self):
        if self.age >= 18:
            return True
        else:
            return False

    def remove_money_from_wallet(self, item):
        self.wallet -= item.price

    def customer_can_buy_drink(self, drink, pub):
        if self.age_challenge() == True:
            if pub.drink_available(drink) == True:
                if self.customer_can_afford_item(drink) == True:
                    self.remove_money_from_wallet(drink)
                    pub.add_money_to_till(drink)
                    pub.remove_item_from_stock(drink)
