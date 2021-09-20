def binomial_coefficient(n: int, m: int, bc: list):
    for i in range(n + 1):
        bc[i][0] = 1
    for j in range(n + 1):
        bc[j][j] = 1
    for i in range(1, n + 1):
        for j in range(1, i):
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j]
    return bc[n][m]


def main():
    n = int(input())
    m = int(input())
    if n < m:
        raise ValueError("The first argument must be greater or equal to the second")

    bc = list()
    for i in range(n + 1):
        bc.append([None for _ in range(i+1)])
    print(binomial_coefficient(n, m, bc))


if __name__ == '__main__':
    main()