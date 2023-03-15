from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @property
    @abstractmethod
    def food_that_eats(self):
        pass

    @property
    @abstractmethod
    def gained_weight(self):
        pass

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def feed(self, food):
        if type(food) not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.gained_weight
        self.food_eaten += food.quantity

class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

