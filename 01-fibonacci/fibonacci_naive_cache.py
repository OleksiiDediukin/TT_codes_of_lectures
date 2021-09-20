cache: list = [None] * 100  # 100 -- максимальное интересуемое "n"
cache[0] = 0
cache[1] = 1


def fibonacci(n: int) -> int:
    if cache[n] is None:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


def main():
    num = int(input())
    print(fibonacci(num))


if __name__ == '__main__':
    main()
