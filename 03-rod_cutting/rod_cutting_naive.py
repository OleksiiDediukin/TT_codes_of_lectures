def cut(n: int, prices: list) -> int:
    if n == 0:
        return 0

    result = 0
    for i in range(1, n + 1):
        result = max(result, prices[i - 1] + cut(n - i, prices))
    return result


def main():
    rod_len = int(input("Enter rod length: "))
    print("Enter price per length")
    prices = list()
    for i in range(rod_len):
        prices.append(int(input(f"{i + 1}: ")))

    print("Result: ", cut(rod_len, prices))


if __name__ == '__main__':
    main()