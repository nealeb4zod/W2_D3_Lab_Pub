class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_money_to_till(self, pub, drink):
        pub.till += drink.price