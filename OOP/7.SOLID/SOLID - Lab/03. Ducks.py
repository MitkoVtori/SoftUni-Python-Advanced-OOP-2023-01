from abc import ABC, abstractmethod


class Animal(ABC):

    @staticmethod
    @abstractmethod
    def make_sound():
        raise NotImplementedError


class Duck(Animal, ABC):

    def __init__(self, name):
        self.name = name

    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck(Duck):

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        """Rubber duck can walk only if you move it"""
        raise Exception('I cannot walk by myself')

    @staticmethod
    def fly():
        """Rubber duck can fly only if you throw it"""
        raise Exception('I cannot fly by myself')

    def __repr__(self):
        return f"{self.name} is a Duck of type {self.__class__.__name__}s"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self, name):
        super().__init__(name)
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()

        else:
            self.height += 1

    def land(self):
        self.height = 0

    def __repr__(self):
        return f"{self.name} is a Duck of type {self.__class__.__name__}s"

