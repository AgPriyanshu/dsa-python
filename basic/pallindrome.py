# Problem Statement: Given an integer N, return true if it is a palindrome else return false.
# A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and
# 4554 are palindromes because they remain the same when their digits are reversed.


def reverse_digits(n):
    result = ""
    if n == 0:
        result = "0"
    while n != 0:
        r = n % 10
        n = n // 10
        result += str(r)
    return int(result)


def pallin(n):
    reverse_n = reverse_digits(n)
    if reverse_n == n:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Pallindrome: ", pallin(1321))
