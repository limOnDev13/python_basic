from collections import Counter


def count_unique_characters(text: str) -> int:
    hist: Counter = Counter()

    for sym in text:
        hist[sym] += 1

    return len(list(filter(lambda symbol: hist[symbol] == 1, hist)))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
