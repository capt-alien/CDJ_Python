#!python3

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name, price, catigory):
        new_product= Products(name, price, catigory)
        self.products.append(new_product)
        return self

    def sell_product(self, name):
        for product in self.products:
            if product.name = name:
                self.products.pop(product)
        return self

    def inflation(self, precent_increase):
        for product in self.products:
            self.product.price == self.product.price * precent_increase
        return self

    def set_clearance(self, catigory, discount):
        for product in self.products:
            if self.product.catigory == catigory:
                self.product.price = self.product.price * (1-discount)
        return self


class Products:
    def __init__(self, name, price, catigory):
        self.name = name
        self.price = price
        self.catigory = catigory

    def update_price(self, change, is_increased = True):
        """updates the product's price. If is_increased is True,
        the price should increase by the percent_change provided.
        If False, the price should decrease by the percent_change provided."""
        if is_increased == True:
            self.price = self.price*(1+change)
        else:
            self.price = self.price*(-1-change)
        return self

    def print_info(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Catigory: ", self.catigory)
