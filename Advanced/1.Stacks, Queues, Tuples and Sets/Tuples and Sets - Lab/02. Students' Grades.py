grades = int(input())

students = {}

for curr_student in range(grades):
    student, grade = input().split()

    if student not in students:
        students[student] = [float(grade)]
        continue

    students[student].append(float(grade))

for student, student_grades in students.items():
    print(student, '->', ' '.join([f'{grade:.2f}' for grade in student_grades]), f'(avg: {sum(student_grades) / len(student_grades):.2f})')



# ---- OLD ----
# student_grades = {}
#
# number_of_grades = int(input())
#
# for grades in range(number_of_grades):
#     name, grade = input().split()
#     if name not in student_grades:
#         student_grades[name] = [f'{float(grade):.2f}']
#         continue
#     student_grades[name].append(f'{float(grade):.2f}')
#
# [print(f'{name} -> {" ".join(grades)} (avg: {sum(list(map(float, grades))) / len(list(map(float, grades))):.2f})') for name, grades in student_grades.items()]
