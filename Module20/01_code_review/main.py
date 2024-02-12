from typing import Any


students: dict[int, dict[str, Any]] = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_interests_and_len_second_names(
        people: dict[int, dict[str, Any]]
) -> tuple[set[str], int]:
    """
    Функция возвращает множество интересов и
    длину всех фамилий студентов.
    :param people: Словарь с информациями о студентах.
    :return: Список интересов и длину всех фамилий.
    """
    # Создадим множество интересов с помощью объединения
    set_interests: set[str] = set()
    total_length: int = 0  # Длина всех фамилий

    for student_info in people.values():
        set_interests = set_interests | set(student_info['interests'])
        total_length += len(student_info['surname'])

    return set_interests, total_length


print('Список пар "ID студента - возвраст":',
      [(student_id, student_info['age'])
       for student_id, student_info in students.items()])

interests, total_len = get_interests_and_len_second_names(
    students
)
print('Полный список интересов всех студентов:',
      interests)
print('Общая длина всех фамилий студентов:',
      total_len)
