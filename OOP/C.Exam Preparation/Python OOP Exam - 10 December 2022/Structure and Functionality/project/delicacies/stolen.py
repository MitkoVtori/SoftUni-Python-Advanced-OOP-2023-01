from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    portion = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.portion, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."

