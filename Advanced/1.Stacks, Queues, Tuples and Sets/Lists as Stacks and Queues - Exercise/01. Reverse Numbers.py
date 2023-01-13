class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def count(self):
        return len(self.stack)


reverse_integers = Stack()

[reverse_integers.push(int(num)) for num in input().split()]
[print(reverse_integers.pop(), end=" ") for _ in range(reverse_integers.count())]