from typing import Generator, Sequence


def analog_zip(first_seq: Sequence, second_seq: Sequence) -> Generator:
    if len(first_seq) > len(second_seq):
        return (
            tuple([first_seq[index], second_seq[index]])
            for index, _ in enumerate(second_seq)
        )
    else:
        return (
            tuple([first_seq[index], second_seq[index]])
            for index, _ in enumerate(first_seq)
        )


string: str = 'abcd'
test_tuple: tuple[int, ...] = (10, 20, 30, 40)

result_generator: Generator = analog_zip(string, test_tuple)
print(result_generator)
for pair in result_generator:
    print(pair)
