schedule = input().split(', ')
while True:
    text = input()
    if text == 'course start':
        break
    text = text.split(':')
    command = text[0]
    lesson = text[1]
    exercise = f'{lesson}-Exercise'
    if command == 'Add':
        if lesson not in schedule:
            schedule.append(lesson)

    elif command == 'Insert':
        i_insert = int(text[2])
        if lesson not in schedule:
            schedule.insert(i_insert, lesson)

    elif command == 'Remove':
        if lesson in schedule:
            schedule.remove(lesson)
            if exercise in schedule:
                schedule.remove(exercise)

    elif command == 'Swap':
        lesson_two = text[2]
        exercise_two = f"{lesson_two}-Exercise"
        if lesson in schedule and lesson_two in schedule:
            index_lesson = schedule.index(lesson)
            index_lesson_two = schedule.index(lesson_two)
            if exercise in schedule and exercise_two in schedule:
                schedule[index_lesson+1], schedule[index_lesson_two+1] = exercise_two, exercise
                schedule[index_lesson], schedule[index_lesson_two] = lesson_two, lesson
            elif exercise_two in schedule:
                schedule[index_lesson], schedule[index_lesson_two] = lesson_two, lesson
                move = schedule.pop(index_lesson_two+1)
                schedule.insert(index_lesson+1, move)
            elif exercise in schedule:
                schedule[index_lesson], schedule[index_lesson_two] = lesson_two, lesson
                move = schedule.pop(index_lesson + 1)
                schedule.insert(index_lesson_two + 1, move)
            else:
                schedule[index_lesson], schedule[index_lesson_two] = lesson_two, lesson

    else:
        if lesson in schedule:
            i_lesson = schedule.index(lesson)
            if exercise not in schedule:
                schedule.insert(i_lesson+1, exercise)
        else:
            if exercise not in schedule:
                schedule.append(lesson)
                schedule.append(exercise)
            # else:
            #     i_exercise = schedule.index(exercise)
            #     schedule.insert(i_exercise-1, lesson)

for i, lesson in enumerate(schedule):
    print(f"{i+1}.{lesson}")