def fibonacci(n: int) -> int:
    data = [0, 1]
    data += [None] * (n-1)

    for i in range(2, n + 1):
        data[i] = data[i - 1] + data[i - 2]

    return data[n]


def main():
    num = int(input())
    print(fibonacci(num))


if __name__ == '__main__':
    main()
