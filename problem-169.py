#E-commerce Cart System

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(product.name, "Added to Cart")

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_cart(self):
        print("Cart Items:")
        for item in self.items:
            print(item.name, "-", item.price)
        print("Total Price:", self.total_price())


# system create
cart = Cart()

p1 = Product("Mobile", 20000)
p2 = Product("Headphone", 2000)

cart.add_product(p1)
cart.add_product(p2)

cart.show_cart()

'''
output:-

Mobile Added to Cart
Headphone Added to Cart
Cart Items:
Mobile - 20000
Headphone - 2000
Total Price: 22000
'''