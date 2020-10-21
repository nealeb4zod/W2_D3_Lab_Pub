class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_money_to_till(self, pub, drink):
        pub.till += drink.price

    def drink_available(self, drink_to_find):
        for drink in self.drinks:
            if drink.name == drink_to_find.name and drink.quantity >=1:
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

    def stock_count(self):
        total_stock = 0
        for drink in self.drinks:
            total_stock += (drink.price * drink.quantity)
        return total_stock

    def check_quantity(self, drink_to_find):
        for drink in self.drinks:
            if drink.name == drink_to_find.name:
                return drink.quantity

    def remove_item_from_stock(self, drink_to_find):
        for drink in self.drinks:
            if drink.name == drink_to_find.name:
                drink.quantity -= drink_to_find.quantity