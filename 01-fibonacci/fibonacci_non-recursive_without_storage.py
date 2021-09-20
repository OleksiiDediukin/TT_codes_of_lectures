def fibonacci(n: int) -> int:
    prev1 = 0
    prev2 = 1
    if n == 0:
        return 0
    for i in range(2, n):
        prev1, prev2 = prev2, prev1 + prev2
        # curr = prev1 + prev2
        # prev1 = prev2
        # prev2 = curr
    return prev1 + prev2


def main():
    num = int(input())
    print(fibonacci(num))


if __name__ == '__main__':
    main()
