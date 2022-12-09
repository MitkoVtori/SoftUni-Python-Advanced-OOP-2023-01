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


numbers_stack = Stack()

lines_of_input = int(input())

min_max_num = []

for num in range(lines_of_input):
    number = input().split()

    if number[0] == '1':
        numbers_stack.push(number[1])
        min_max_num.append(int(number[1]))

    elif numbers_stack.count():
        if number[0] == '2':
            numbers_stack.pop()
            min_max_num.pop()

        elif number[0] == '3':
            print(max(min_max_num))

        elif number[0] == '4':
            print(min(min_max_num))

numbers = [str(num) for num in min_max_num[::-1]]

print(', '.join(numbers))