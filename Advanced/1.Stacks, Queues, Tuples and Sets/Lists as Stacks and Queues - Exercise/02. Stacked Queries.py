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


stack = Stack()
numbers_list = []

lines = int(input())

for queries in range(lines):
    query = input()

    if query.startswith("1"):
        num = int(query.split()[1])
        stack.push(num)
        numbers_list.append(num)

    elif query == "2":
        if stack.count():
            stack.pop()
            numbers_list.pop()

    elif query == "3":
        if stack.count():
            print(max(numbers_list))

    elif query == "4":
        if stack.count():
            print(min(numbers_list))


print(", ".join([str(stack.pop()) for _ in range(stack.count())]))