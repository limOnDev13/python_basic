nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result_list: list[int] = [
    number
    for first_list in nice_list
    for second_list in first_list
    for number in second_list
]
print(result_list)
