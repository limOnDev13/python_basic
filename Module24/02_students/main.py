from random import randint
from service import servise


class Student:

    def __init__(self, name: str, group: int, grade: dict[str, int]):
        self.full_name: str = name
        self.group_num: int = group
        self.grade: dict[str, int] = grade  # Успеваемость имеет вид словаря,
        # где ключи - название предметов, значения - оценки

    def average_grade(self) -> float:
        """
        Метод возвращает средний балл.
        :return: Средний балл.
        """
        return round(sum(self.grade.values()) / len(self.grade), 2)

    def print_info(self):
        print('Имя: {name}\nНомер группы: {group}\nУспеваемость: {grade}\n'
              'Средний балл: {average_grade}'.format(
                name=self.full_name,
                group=self.group_num,
                grade=self.grade,
                average_grade=self.average_grade()))
        print()


def random_grades(subjects: list[str]) -> dict[str, int]:
    """
    Метод генерирует случайные успеваемости.
    :param subjects: Список предметов.
    :return: Словарь с успеваемостью.
    """
    return {
        subject: randint(1, 5)
        for subject in subjects
    }


def print_students_info(students_list: list[Student]):
    """
    Метод выводит в консоль информацию о студентах.
    :param students_list: Список студентов.
    :return: Ничего
    """
    for student in students_list:
        student.print_info()


subjects: list[str] = ['Math', 'Physics', 'History', 'Biology', 'Russian']
students: list[Student] = [
    Student(name=servise.generate_word(),
            group=randint(1, 100),
            grade=random_grades(subjects))
    for _ in range(10)
]

# До сортировки
print_students_info(students)
print('-' * 100)
# После сортировки
students.sort(key=lambda x: x.average_grade())
print_students_info(students)
