groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 5, 3]
    },
    {
        "name": "Дарья",
        "surname": "Кузнецова",
        "exams": ["География", "HNE", "КТП"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Мария",
        "surname": "Кнутарева",
        "exams": ["Физика", "H<NG", "КТП"],
        "marks": [3, 3, 3]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)


def filter_students_by_avg_mark(students):
    try:
        x = float(input("Введите средний балл для фильтрации: "))
    except ValueError:
        print("Ошибка: введите число")
        return

    filtered_students = []

    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > x:
            filtered_students.append((student["name"], student["surname"], avg_mark))

    if filtered_students:
        print(f"Студенты с средним баллом выше {x}:")
        for name, surname, avg in filtered_students:
            print(f"{name} {surname} - Средний балл: {avg:.2f}")
    else:
        print(f"Нет студентов со средним баллом выше {x}.")


# Вызов функции
filter_students_by_avg_mark(groupmates)
