class Stack:

    def __init__(self):
        self.stack = [int(num) for num in input().split()]

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def count(self):
        return len(self.stack)


clothes = Stack()
capacity_per_rack = int(input())

racks_used = 1

sum_clothes = 0
while clothes.count():

    if clothes.peek() + sum_clothes <= capacity_per_rack:
        sum_clothes += clothes.pop()

    elif clothes.peek() + sum_clothes > capacity_per_rack:
        racks_used += 1
        sum_clothes = clothes.pop()

print(racks_used)