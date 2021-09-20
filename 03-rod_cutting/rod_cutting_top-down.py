import functools
import random

prices = list()


@functools.lru_cache(None)  # About lru_cache: https://tirinox.ru/lru-cache/
def cut(n: int) -> int:
    result = 0
    for i in range(1, n + 1):
        result = max(result, prices[i - 1] + cut(n - i))
    return result


def main():
    rod_len = int(input("Enter rod length: "))
    prices.extend([random.randint(1, 100) for _ in range(rod_len)])
    print("Prices: ", prices if len(prices) < 20 else prices[:8] + ["..."] + prices[-8:])
    print("Result: ", cut(rod_len))


if __name__ == '__main__':
    main()