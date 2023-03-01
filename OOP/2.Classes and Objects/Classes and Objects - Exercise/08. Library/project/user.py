from typing import List


class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []

    def info(self):
        return ', '.join(sorted(self.books))

    def __repr__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

