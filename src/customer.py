class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def customer_can_afford_drink(self, customer, drink):
        if customer.wallet >= drink.price:
            return True
        else:
            return False

    def remove_money_from_wallet(self, customer, drink):
        customer.wallet -= drink.price

    def customer_can_buy_drink(self, customer, drink, pub):
        if self.customer_can_afford_drink(customer, drink) == True:
            self.remove_money_from_wallet(customer, drink)
            pub.add_money_to_till(pub, drink)