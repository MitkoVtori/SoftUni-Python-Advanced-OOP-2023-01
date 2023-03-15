from project.animal import Animal


class Cat(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

