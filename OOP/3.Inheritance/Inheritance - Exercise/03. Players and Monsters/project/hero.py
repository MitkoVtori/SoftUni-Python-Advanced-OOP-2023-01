class Hero:

    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self):
        return f"{self.username} of type {Hero.__name__} has level {self.level}"

