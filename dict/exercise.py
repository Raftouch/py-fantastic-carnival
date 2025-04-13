students = [
    {"name": "Bob", "surname": "Brown", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Pitt", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gatemy", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Ann", "surname": "Ross", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Ilona", "surname": "Massimi", "grades": None}
]


def get_best_students(*, students: list[dict]) -> list[dict]:
    best_students = []
    highest_avg = 0

    for student in students:
        grades = student["grades"]

        if grades is None or len(grades) == 0:
            average_grade = 0
        else:
            average_grade = sum(grades) / len(grades)

        if average_grade > highest_avg:
            highest_avg = average_grade
            best_students = [student]
        elif average_grade == highest_avg:
            best_students.append(student)

    return best_students
    # result = "Best students are: "
    # bs_names = [f"{bs["name"]} {bs["surname"]}" for bs in best_students]
    # return result + ", ".join(bs_names)


print(get_best_students(students=students))