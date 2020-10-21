class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_money_to_till(self, pub, drink):
        pub.till += drink.price

    def drink_available(self, drink_to_find):
        for drink in self.drinks:
            if drink.name == drink_to_find.name:
                return True

    def age_challange(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def check_drunkenness(self, customer):
        if customer.drunkenness >= 10:
            return True
        else:
            return False