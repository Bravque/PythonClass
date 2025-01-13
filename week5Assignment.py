############### Assignment 1 ###################

class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def __str__(self):
        return f"Smartphone(Brand: {self.brand}, Model: {self.model}, Price: ${self.price})"


# Inheritance Layer
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life  # Additional attribute for Smartwatch

    def track_steps(self, steps):
        return f"Tracking {steps} steps using {self.brand} {self.model}."

    def __str__(self):
        return f"Smartwatch(Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Battery Life: {self.battery_life} hours)"


# Example usage
phone = Smartphone("Apple", "iPhone 14", 999)
print(phone)
print(phone.make_call("123-456-7890"))
print(phone.send_message("123-456-7890", "Hello!"))

watch = Smartwatch("Samsung", "Galaxy Watch 6", 399, 48)
print(watch)
print(watch.track_steps(5000))

############## Activity 1  ####################

class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Function to demonstrate polymorphism
def demonstrate_movement(vehicle):
    print(f"The vehicle is: {vehicle.move()}")


# Example usage
car = Car()
plane = Plane()
boat = Boat()

demonstrate_movement(car)
demonstrate_movement(plane)
demonstrate_movement(boat)
