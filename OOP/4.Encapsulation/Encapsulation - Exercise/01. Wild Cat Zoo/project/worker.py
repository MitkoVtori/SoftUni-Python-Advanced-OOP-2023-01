class Worker:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

