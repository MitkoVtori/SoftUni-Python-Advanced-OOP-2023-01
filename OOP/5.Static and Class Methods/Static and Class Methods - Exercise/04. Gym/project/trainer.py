from project.class_id_mixin import ClassIdMixin


class Trainer(ClassIdMixin):
    id = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

