# n = int(input())
# student_academy = {}
# for _ in range(n):
#     key = input()
#     value = float(input())
#     if key not in student_academy:
#         student_academy[key] = []
#     student_academy[key].extend([value])
# for key, value in student_academy.items():
#     averige_grade = sum(student_academy[key])/len(student_academy[key])
#     if averige_grade >= 4.50:
#         print(f'{key} -> {averige_grade:.2f}')

from statistics import mean
n = int(input())
student_academy = {}
for _ in range(n):
    key = input()
    value = float(input())
    if key not in student_academy:
        student_academy[key] = []
    student_academy[key].extend([value])

[print(f'{key} -> {mean(student_academy[key]):.2f}')
 for key in student_academy.keys()
 if mean(student_academy[key]) >= 4.50]