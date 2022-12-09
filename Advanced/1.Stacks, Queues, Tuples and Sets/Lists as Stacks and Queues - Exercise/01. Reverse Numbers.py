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

integers = [int(num) for num in input().split()]

for number in integers:
    reverse_integers.push(number)

while reverse_integers.count():
    print(reverse_integers.pop(), end=' ')