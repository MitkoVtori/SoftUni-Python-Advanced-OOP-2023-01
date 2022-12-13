first_sequence = set((map(int, input().split())))
second_sequence = set((map(int, input().split())))

command_lines = int(input())

for row in range(command_lines):

    command = input().split()
    command[0] += f" {command[1]}"
    command.pop(1)

    numbers = set([int(num) for num in command[1:]])

    if command[0] == "Add First":
        [first_sequence.add(num) for num in numbers]

    elif command[0] == "Add Second":
        [second_sequence.add(num) for num in numbers]

    elif command[0] == "Remove First":
        [first_sequence.remove(num) for num in numbers if num in first_sequence]

    elif command[0] == "Remove Second":
        [second_sequence.remove(num) for num in numbers if num in second_sequence]

    elif command[0] == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
            continue
        print(False)

print(", ".join([str(num) for num in sorted(first_sequence)]))
print(", ".join([str(num) for num in sorted(second_sequence)]))
