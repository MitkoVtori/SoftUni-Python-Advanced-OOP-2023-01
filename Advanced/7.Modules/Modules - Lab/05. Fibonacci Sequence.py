from custom_module.fibonacci_sequence import create_sequence, locate

operations = {
    "Create": create_sequence,
    "Locate": locate
}

command = input()
while command != "Stop":

    operation, *rest = command.split()
    print(operations[operation](int(rest[-1])))

    command = input()
