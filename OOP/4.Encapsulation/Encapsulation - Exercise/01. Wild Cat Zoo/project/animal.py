class Animal:

    def __init__(self, name, gender, age, money_for_care):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

