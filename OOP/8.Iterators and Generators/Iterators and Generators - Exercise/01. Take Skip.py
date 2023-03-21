class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.current_number = self.step
        self.count = count
        self.operations_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.operations_count += 1
        if self.operations_count <= self.count:
            number = self.current_number
            self.current_number += self.step
            return number - self.step
        else:
            raise StopIteration()

