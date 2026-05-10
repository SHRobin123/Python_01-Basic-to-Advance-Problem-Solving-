#Inventory System (Product Management)

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def show(self):
        print(self.name, "- Stock:", self.stock)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, stock):
        p = Product(name, stock)
        self.products.append(p)

    def sell_product(self, name, qty):
        for p in self.products:
            if p.name == name:
                if p.stock >= qty:
                    p.stock -= qty
                    print(qty, name, "Sold")
                else:
                    print("Not enough stock")
                return
        print("Product not found")

    def show_inventory(self):
        print("Inventory List:")
        for p in self.products:
            p.show()


# system create
inv = Inventory()

inv.add_product("Rice", 50)
inv.add_product("Oil", 30)

inv.sell_product("Rice", 10)

inv.show_inventory()

'''
output:-

10 Rice Sold
Inventory List:
Rice - Stock: 40
Oil - Stock: 30
'''