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


parentheses = Stack()
expression = input()

for index, char in enumerate(expression):

    if char == "(":
        parentheses.push(index)

    elif char == ")":
        opening_bracket = parentheses.pop()
        closing_bracket = index
        print(expression[opening_bracket:closing_bracket+1])