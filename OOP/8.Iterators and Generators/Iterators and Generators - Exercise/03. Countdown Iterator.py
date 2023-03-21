class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.current_number = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number >= 0:
            self.current_number -= 1
            return self.current_number + 1
        else:
            raise StopIteration()

