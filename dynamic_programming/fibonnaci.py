memoize = {}


def fib(number: int) -> int:
    if number <= 1:
        return number
    elif memoize.get(number) is not None:
        return memoize[number]
    else:
        memoize[number] = fib(number - 1) + fib(number - 2)
        return memoize[number]


def fib_table(number: int, dp: list):
    dp[0] = 1
    dp[1] = 1

    for n in range(2, number + 1):
        dp[n] = dp[n - 1] + dp[n - 2]

    print(dp[n])


if __name__ == "__main__":
    # fib(6)
    # print(len(memoize))
    fib_table(5, [-1] * 6)
