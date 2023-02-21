class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        if self.quantity + amount <= self.size:
            self.quantity += amount

    def status(self):
        return self.size - self.quantity

