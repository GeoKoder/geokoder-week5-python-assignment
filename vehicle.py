# Base class (optional)
class Vehicle:
    def move(self):
        pass  # General idea of movement


# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing through water 🚢")


# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each object calls its own move() method
