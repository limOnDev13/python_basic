from random import uniform


length: int = 20
first_team: list[float] = [round(uniform(5, 10), 2) for _ in range(length)]
second_team: list[float] = [round(uniform(5, 10), 2) for _ in range(length)]

winners: list[float] = [(first_team[i] if first_team[i] > second_team[i] else second_team[i]) for i in range(length)]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winners)
