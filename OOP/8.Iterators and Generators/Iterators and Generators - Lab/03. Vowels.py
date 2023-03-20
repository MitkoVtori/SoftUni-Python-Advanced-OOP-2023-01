class vowels:

    def __init__(self, string):
        self.vowels = ['a', 'e', 'i', 'u', 'y', 'o']
        self.string = ''.join([x for x in string if x.lower() in self.vowels])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self.index
        if i < len(self.string):
            self.index += 1
            return self.string[i]
        else:
            raise StopIteration()

