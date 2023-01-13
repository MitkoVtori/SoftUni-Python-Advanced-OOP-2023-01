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


pairs = {
    '{': '}',
    '(': ')',
    '[': ']'
}

bracket_integers = Stack()
parentheses = input()

balanced = True

for index, bracket in enumerate(parentheses):

    if bracket in pairs.keys():
        bracket_integers.push(index)

    elif bracket in pairs.values():
        if bracket_integers.count():

            last_index = bracket_integers.peek()

            if bracket == pairs[parentheses[last_index]]:
                bracket_integers.pop()

            else:
                balanced = False

        else:
            balanced = False

    if not balanced:
        break

if balanced:
    print('YES')

elif not balanced:
    print("NO")