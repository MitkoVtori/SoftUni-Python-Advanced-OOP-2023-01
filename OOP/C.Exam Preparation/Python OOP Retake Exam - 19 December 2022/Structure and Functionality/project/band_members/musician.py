from abc import ABC, abstractmethod


class Musician(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Musician name cannot be empty!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musician should be at least 16 years old!")

        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill):
        pass

