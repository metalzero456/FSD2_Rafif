class Dog:
    # Class attribute
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"
    def bark(self):
        return f"{self.name} says Bark Bark Bark"

class Bulldog(Dog):
    def bark(self, sound="Grr grr grr"):
        return f"{self.name} says {sound}"
    pass

miles = Dog("Miles", 4)
jimmy = Bulldog("Jimmy", 5)

print(miles.description())
print(miles.bark())
print(jimmy.description())
print(jimmy.bark())
print(isinstance(jimmy, Dog))