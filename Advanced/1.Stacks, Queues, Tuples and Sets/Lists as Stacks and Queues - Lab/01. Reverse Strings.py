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

for char in string:
    reverser.push(char)

reversed_string = ''

while reverser.count():
    reversed_string += reverser.pop()

print(reversed_string)