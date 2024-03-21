from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return f"{self.make} {self.model} starts the engine."

    def stop(self):
        return f"{self.make} {self.model} stops the engine."

class Motorcycle(Vehicle):
    def start(self):
        return f"{self.make} {self.model} revs the engine."

    def stop(self):
        return f"{self.make} {self.model} shuts off the engine."

class Truck(Vehicle):
    def start(self):
        return f"{self.make} {self.model} cranks the engine."

    def stop(self):
        return f"{self.make} {self.model} turns off the engine."

# Creating instances of concrete classes
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR600RR")
truck = Truck("Ford", "F-150")

# Using abstraction to perform actions on vehicles
print(car.start())        # Output: Toyota Camry starts the engine.
print(motorcycle.stop())  # Output: Honda CBR600RR shuts off the engine.
print(truck.start())      # Output: Ford F-150 cranks the engine.
