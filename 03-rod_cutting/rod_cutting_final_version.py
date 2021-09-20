import functools
import random

# массив цен стержней:
prices = list()

# массив результатов
results = list()

# массив оптимальных размеров первой части
splits = list()


@functools.lru_cache(None)  # About lru_cache: https://tirinox.ru/lru-cache/
def cut(n: int) -> int:
    results[0] = 0
    for j in range(1, n + 1):
        result = -1
        for i in range(1, j + 1):
            candidate = prices[i - 1] + results[j - i]
            if candidate > result:
                result = candidate
                splits[j] = i
        results[j] = result
    return results[n]


def main():
    rod_len = int(input("Enter rod length: "))
    prices.extend([random.randint(1, 100) for _ in range(rod_len)])
    results.extend([None] * (rod_len + 1))
    splits.extend([None] * (rod_len + 1))
    print("Prices: ", prices if len(prices) <= 20 else prices[:8] + ["..."] + prices[-8:])
    print("Result: ", cut(rod_len))


if __name__ == '__main__':
    main()
