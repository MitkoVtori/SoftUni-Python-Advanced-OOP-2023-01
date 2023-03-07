from project.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories
