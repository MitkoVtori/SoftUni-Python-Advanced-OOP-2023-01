from collections import deque


class Stack:

    def __init__(self, items):
        self.stack = list(items)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def count(self):
        return len(self.stack)

    def __repr__(self):
        return ', '.join([str(item) for item in self.stack])


class MathOperations:

    def __init__(self, bee, nectar):
        self.bee = bee
        self.nectar = nectar

    def multiply(self):
        return abs(self.bee * self.nectar)

    def divide(self):
        return abs(self.bee / self.nectar)

    def add(self):
        return abs(self.bee + self.nectar)

    def subtract(self):
        return abs(self.bee - self.nectar)


working_bees = deque(map(int, input().split()))
nectar = Stack(map(int, input().split()))
process = deque(input().split())

total_honey = 0

while working_bees and nectar.count():

    current_bee = working_bees[0]
    current_nectar = nectar.peek()

    if current_bee <= current_nectar:

        if process[0] == "*":
            total_honey += MathOperations(current_bee, current_nectar).multiply()

        elif process[0] == "/" and current_nectar > 0:
            total_honey += MathOperations(current_bee, current_nectar).divide()

        elif process[0] == "+":
            total_honey += MathOperations(current_bee, current_nectar).add()

        elif process[0] == "-":
            total_honey += MathOperations(current_bee, current_nectar).subtract()

        working_bees.popleft()
        nectar.pop()
        process.popleft()

    elif current_bee > current_nectar:
        nectar.pop()
        continue

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join([str(num) for num in working_bees])}")

if nectar.count():
    print(f"Nectar left: {nectar}")