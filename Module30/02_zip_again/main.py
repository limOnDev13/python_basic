letters: list[str] = ['a', 'b', 'c', 'd', 'e']
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]

my_list: list[tuple[str, int]] = list(map(lambda let, num: (let, num), letters, numbers))
print(my_list)
