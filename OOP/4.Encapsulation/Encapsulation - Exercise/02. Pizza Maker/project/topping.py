class Topping:

    # def __init__(self, topping_type, weight):
    #     if topping_type == '':
    #         raise ValueError("The topping type cannot be an empty string")
    #     if weight <= 0:
    #         raise ValueError("The weight cannot be less or equal to zero")
    #
    #     self.topping_type = topping_type
    #     self.weight = weight

    def __init__(self, topping_type, weight):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        if value == '':
            raise ValueError("The topping type cannot be an empty string")

        self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")

        self.__weight = value

