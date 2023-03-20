class reverse_iter:

    def __init__(self, iterable):
        self.iter = iterable[::-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
         i = self.index
         if i < len(self.iter):
             self.index += 1
             return self.iter[i]
         else:
             raise StopIteration()

