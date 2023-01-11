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


reverser = Stack()

string = input()

[reverser.push(char) for char in string]
[print(reverser.pop(), end="") for _ in range(len(string))]