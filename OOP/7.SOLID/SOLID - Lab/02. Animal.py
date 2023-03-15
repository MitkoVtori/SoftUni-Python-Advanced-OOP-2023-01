from abc import ABC, abstractmethod


class Animal(ABC):

    @staticmethod
    @abstractmethod
    def make_sound():
        raise NotImplementedError

class Dog(Animal):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def make_sound():
        return "Woof!"

    def __repr__(self):
        return f"{self.name} is {self.age} years old {self.gender} {self.__class__.__name__}"


class Cat(Animal):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def make_sound():
        return "Meow!"

    def __repr__(self):
        return f"{self.name} is {self.age} years old {self.gender} {self.__class__.__name__}"


animals = [Cat("Citty", 2, "Female"), Dog("Rocky", 8, "Male")]
for animal in animals:
    print(animal.make_sound())
    print(animal)

print(Animal.make_sound()) # Must get an Error
