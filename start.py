""" 
Encapsulation: Encapsulation is the concept of bundling data (attributes) and methods (functions)
 that operate on that data into a single unit (class). It hides the internal details of how an object works,
   and you can access or modify its data through methods.

Inheritance: Inheritance allows you to create a new class (subclass or derived class)
 by inheriting properties and methods from an existing class (base class or superclass).
 This promotes code reuse.
"""

class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def walk(self):
        print(f"{self.name} is walking")

class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def bark(self):
        print(f"{self.name} is barking")

    def introduce(self):
        print(
            f"My pets name is {self.name}, its a large {self.color} {self.breed} and despite it being just {self.age} years old"
        )


pet = Dog("andie", "rotwiler", 10, "grey")


# inheritance
""" so the first dog class is the parent of the dummydog class i.e
all attributes of the parent class can be accecced by the dummy dog class
 """

class DummyDog(Dog):
    def __innit__(self,name):
        super().__init__(name)

    def jump(self):
        print(f"{self.name} is jumping around")

pet2 = DummyDog("dumpsta","German Sherpherd",6,"grey",)
print(pet2.age)
print(pet2.bark())








