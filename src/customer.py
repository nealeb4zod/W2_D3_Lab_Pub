class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def make_drunk(self, drink):
        self.drunkenness += drink.alcohol_level

    def customer_can_afford_drink(self, customer, drink):
        if customer.wallet >= drink.price:
            return True
        else:
            return False


    def remove_money_from_wallet(self, customer, drink):
        customer.wallet -= drink.price

    def customer_can_buy_drink(self, customer, drink, pub):
        if pub.age_challange(customer) == True:
            if pub.drink_available(drink) == True:
                if self.customer_can_afford_drink(customer, drink) == True:
                    self.remove_money_from_wallet(customer, drink)
                    pub.add_money_to_till(pub, drink)