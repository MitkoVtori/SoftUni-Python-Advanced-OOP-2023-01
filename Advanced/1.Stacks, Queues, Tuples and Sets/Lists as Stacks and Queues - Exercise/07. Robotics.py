from collections import deque


def read_robots():
    global robots

    robotics = input().split(";")
    robots = {}
    for name_seconds in robotics:
        name, seconds = name_seconds.split('-')
        robots[name] = int(seconds)


def name_robots():
    global available_robots
    available_robots = [key for key in robots.keys()]


def starting_time():
    starting_time_parts = [int(num) for num in input().split(':')]
    time_seconds = in_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])
    return time_seconds


def in_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def read_products():
    deque_products = deque()
    product = input()
    while product != "End":
        deque_products.append(product)
        product = input()
    return deque_products


read_robots()
name_robots()
time_in_seconds = starting_time()
products = read_products()

processing_robots = {}

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    length_processing_robots = processing_robots.copy()

    for robot_name in length_processing_robots:
        processing_robots[robot_name] -= 1

        if processing_robots[robot_name] == 0:
            del processing_robots[robot_name]

    current_product = products.popleft()

    for robot in available_robots:
        if robot not in processing_robots:
            print(f"{robot} - {current_product} [{time(time_in_seconds)}]")
            processing_robots[robot] = robots[robot]
            break
    else:
        products.append(current_product)