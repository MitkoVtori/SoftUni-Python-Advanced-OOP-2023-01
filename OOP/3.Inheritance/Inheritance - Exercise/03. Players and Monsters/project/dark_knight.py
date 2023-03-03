from project.knight import Knight


class DarkKnight(Knight):
    def __str__(self):
        return f"{self.username} of type {DarkKnight.__name__} has level {self.level}"

