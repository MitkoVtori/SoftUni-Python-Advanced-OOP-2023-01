class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.current_row = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_row += 1
        if self.index < len(self.sequence) and self.current_row <= self.number:
            self.index += 1
            return self.sequence[self.index-1]
        elif self.current_row <= self.number:
            self.index = 1
            return self.sequence[self.index-1]
        else:
            raise StopIteration()

