from abc import ABC, abstractmethod


class BaseService(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = [] # robot objects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.rstrip() == "":
            raise ValueError("Service name cannot be empty!")

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

        self.__capacity = value

    @abstractmethod
    def details(self):
        pass

