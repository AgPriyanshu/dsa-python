# Problem Statement: Given an integer N return the reverse of the given number.
def reverse_digits(n):
    result = ""
    if n == 0:
        result = "0"
    while n != 0:
        r = n % 10
        n = n // 10
        result += str(r)
    return int(result)


if __name__ == "__main__":
    print(reverse_digits(1))
