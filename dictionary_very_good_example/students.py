courses = {}
while True:
    text = input()
    if sum(i.isdigit() for i in text) == 0:
        needed_course = text.replace('_', ' ')
        list_of_people = courses[needed_course]
        for i in range(0, len(list_of_people), 2):
            name = list_of_people[i]
            password = list_of_people[i+1]
            print(f'{name} - {password}')
        break
    elements = text.split(':')
    name = elements[0]
    password = elements[1]
    course = elements[2]
    if course not in courses:
        courses[course] = []
    courses[course].extend([name, password])