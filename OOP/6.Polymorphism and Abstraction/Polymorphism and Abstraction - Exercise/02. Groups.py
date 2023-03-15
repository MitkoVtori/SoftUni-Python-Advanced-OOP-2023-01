class Person:
    def __init__(self, name, surname):
        self.surname = surname
        self.name = name

    def __add__(self, obj):
        return Person(self.name, obj.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.people = people
        self.name = name

    def __len__(self):
        return len(self.people)

    def __add__(self, obj):
        return Group(f"{self.name} {obj.name}", self.people + obj.people)

    def __getitem__(self, index):
        return f"Person {index}: {str(self.people[index])}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"

