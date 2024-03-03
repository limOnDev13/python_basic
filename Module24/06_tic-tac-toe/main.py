from dataclasses import dataclass
from typing import Literal


# 1. Класс, который будет описывать одну клетку поля:
@dataclass
class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    number: int
    is_occupied: bool = False


# 2. Класс, который будет описывать поле игры.
class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.cells: list[Cell] = [Cell(num_cell) for num_cell in range(9)]

    def clear(self):
        """
        Метод очищает доску.
        :return:
        """
        for cell in self.cells:
            cell.is_occupied = False


# 3. Класс, который описывает поведение игрока:
class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self, name: str, board: Board):
        self.name: str = name
        self.personal_cells: list[int] = list()  # Хранит номера клеток, на которые сходил игрок
        self.board: Board = board

    def move(self) -> int:
        """
        Метод предлагает игроку выбрать, на какую клетку сходить.
        :return:
        """
        try:
            move_x: int = int(input('Введите номер столбца (1 - 3): ')) - 1
            move_y: int = int(input('Введите номер строки (1 - 3): ')) - 1
            cell_num: int = move_y * 3 + move_x

            if move_x not in [0, 1, 2] or move_y not in [0, 1, 2]:
                raise KeyError('Пожалуйста, введите числа 1, 2 или 3')
            if self.board.cells[cell_num].is_occupied:
                raise IndexError('Данная клетка уже занята!')
        except (KeyError, IndexError) as exc:
            print(exc)
            self.move()
        except ValueError:
            print('Не могу понять, что вы ввели. Пожалуйста, введите числа 1, 2 или 3')
            self.move()
        else:
            self.board.cells[cell_num].is_occupied = True
            self.personal_cells.append(cell_num)
            return cell_num

    def clear(self):
        """
        Метод очищает сохраненные клетки игрока.
        :return: Ничего.
        """
        self.personal_cells = list()


# 4. Класс, который управляет ходом игры:
class Game:
    winning_combos: list[set[int]] = [
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  # строки
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  # столбцы
        {0, 4, 8}, {2, 4, 6}  # диагонали
    ]

    # класс «Игры» содержит атрибуты:
    def __init__(self, player_1: Player, player_2: Player, board: Board):
        # состояние игры,
        self.status: bool = False  # False - игра не запущена, True - запущена
        # игроки,
        self.player1: Player = player_1
        self.player2: Player = player_2
        # счет,
        self.score: dict[int, int] = {1: 0, 2: 0}
        # поле.
        self.board: Board = board
        # очередь первого или второго
        self.turn_first: bool = True

    # А также методы:
    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле,
    # проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.

    def _check_win(self, player: Player) -> bool:
        """
        Метод проверяет, содержит ли игрок выигрышные комбинации.
        :param player: Объект игрока
        :return: True, если у игрока есть выигрышные комбинации.
        """
        for win_combo in self.winning_combos:
            if win_combo & set(player.personal_cells) == win_combo:
                return True
        return False

    def draw_board(self):
        """
        Метод рисует доску (для наглядности).
        :return: Ничего
        """
        for y in range(3):
            for x in range(3):
                cell_num: int = y * 3 + x
                if cell_num in self.player1.personal_cells:
                    print(1, end='\t')
                elif cell_num in self.player2.personal_cells:
                    print(2, end='\t')
                else:
                    print(0, end='\t')
            print()

    def one_move(self) -> Literal[0, 1, 2] | None:
        """
        Метод отвечает за один ход в игре.
        :return: 0 - если ничья, 1 - если выиграл игрок 1, 2 - если выиграл игрок 2, если игра продолжается - None.
        """
        if self.turn_first:
            self.player1.move()
            self.turn_first = False
        else:
            self.player2.move()
            self.turn_first = True

        # Нарисуем доску для наглядности
        self.draw_board()

        # проверим, содержит ли клетки игрока выигрышные комбинации
        if self._check_win(self.player1):
            return 1
        elif self._check_win(self.player2):
            return 2
        elif all([cell.is_occupied for cell in self.board.cells]):
            return 0
        else:
            return None

    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой,
    # который завершается победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.
    def one_game(self):
        """
        Метод запуска одной игры. Очищает поле, запускает цикл с игрой,
        который завершается победой одного из игроков или ничьей.
        :return: Ничего. По условию метод должен возвращать bool, но в моем решении всегда будет True.
        """
        # очистим поле и ходы игроков
        self.board.clear()
        self.player1.clear()
        self.player2.clear()

        # запустим цикл игры
        self.status = True
        game_result: Literal[0, 1, 2] | None = self.one_move()
        while game_result is None:
            game_result = self.one_move()

        # изменим счет
        if game_result == 0:
            self.score[1] += 1
            self.score[2] += 1
        elif game_result == 1:
            self.score[1] += 1
        else:
            self.score[2] += 1

        # изменим статус игры
        self.status = False

    def main(self):
        """
        Основной метод запуска игр.
        В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть.
        После каждой игры выводится текущий счёт игроков.
        :return: Ничего.
        """
        while True:
            self.one_game()
            print('Текущий счет:\n{}: {}\n{}: {}'.format(
                self.player1.name, self.score[1], self.player2.name, self.score[2]
            ))
            # Спросим, нужно ли продолжить игру
            while True:
                try:
                    answer: str = input('Хотите продолжить? (да / нет): ').lower()
                    if answer not in ['да', 'нет']:
                        raise ValueError('Я вас не понял...')
                except ValueError as exc:
                    print(exc)
                else:
                    if answer == 'нет':
                        exit()
                    else:
                        break


board: Board = Board()
first_player: Player = Player(name=input('Введите имя первого игрока: '),
                              board=board)
second_player: Player = Player(name=input('Введите имя второго игрока: '),
                               board=board)
game: Game = Game(first_player, second_player, board)
game.main()
