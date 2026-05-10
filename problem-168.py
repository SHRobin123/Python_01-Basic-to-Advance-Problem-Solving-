#Car Rental System

class Car:
    def __init__(self, name):
        self.name = name
        self.available = True

    def show(self):
        status = "Available" if self.available else "Rented"
        print(self.name, "-", status)


class RentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, name):
        c = Car(name)
        self.cars.append(c)

    def rent_car(self, name):
        for c in self.cars:
            if c.name == name and c.available:
                c.available = False
                print(name, "Rented Successfully")
                return
        print("Car not available")

    def return_car(self, name):
        for c in self.cars:
            if c.name == name:
                c.available = True
                print(name, "Returned")
                return

    def show_cars(self):
        print("Car List:")
        for c in self.cars:
            c.show()


# system create
system = RentalSystem()

system.add_car("Toyota")
system.add_car("Honda")

system.rent_car("Toyota")
system.return_car("Toyota")

system.show_cars()

'''
output:-

Toyota Rented Successfully
Toyota Returned
Car List:
Toyota - Available
Honda - Available
'''