class Product:
    # Constructor
    def __init__(self, name, price=0):
        # Object attributes
        self.name = name
        self.price = price  # private attribute

    def print_details(self):
        print(f"Name = {self.name}, Price = {self.price}")

    def set_price(self, price):
        if price > 0:
           self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


p1 = Product("iPhone X", 80000)
p2 = Product("iPhone X", 80000)
print(p1 == p2)


