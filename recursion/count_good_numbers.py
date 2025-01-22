def countGoodNumbers(digit: int, i: int, n: int) -> int:
    print([digit, i, n])
    if i == n - 1:
        return 1

    elif not (
        (i % 2 == 0 and digit % 2 == 0) or (i % 2 != 0 and digit in [2, 3, 5, 7])
    ):
        return 0

    count = 0

    for j in range(digit, 9):
        for k in range(i + 1, n - i):
            count += countGoodNumbers(j, k, n)
    return count


if __name__ == "__main__":
    print(countGoodNumbers(0, 0, 2))
