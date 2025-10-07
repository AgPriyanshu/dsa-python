# Problem Statement: "Given a string, check if the string is palindrome or not."
# A string is said to be palindrome if the reverse of the string is the same as the string.
def check_pallindrome(string: str, i, j):
    if i >= j:
        return True

    if not string[i].isalnum():
        return check_pallindrome(string, i + 1, j)
    elif not string[j].isalnum():
        return check_pallindrome(string, i, j - 1)

    if string[i].lower() != string[j].lower():
        return False

    return check_pallindrome(string, i + 1, j - 1)


if __name__ == "__main__":
    string = "aa"
    print(check_pallindrome(string, 0, len(string) - 1))
