from collections import deque
from time import sleep

rows, columns = 10, 3
snake = "Python"

while True:

    index_snake = 0

    for row in range(rows):

        result = deque()

        for col in range(columns):

            if index_snake == len(snake):
                index_snake = 0

            if row % 2 == 0:
                result.append(snake[index_snake])

            else:
                result.appendleft(snake[index_snake])

            index_snake += 1

        print("".join(result))
        sleep(0.1)