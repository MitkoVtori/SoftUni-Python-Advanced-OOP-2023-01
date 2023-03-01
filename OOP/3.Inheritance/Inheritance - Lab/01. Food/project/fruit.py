from project.food import Food


class Fruit(Food):

    def __init__(self, name, expiration_date):
        self.name = str(name)
        self.expiration_date = str(expiration_date)

