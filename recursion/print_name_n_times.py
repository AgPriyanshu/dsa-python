# Problem: Print your Name N times using recursion


def print_n_times(count, n, name="Priyanshu"):
    if count > n:
        return
    print(name)
    print_n_times(count + 1, n)


def print_recur(name: str, index):
    if index == (len(name) - 1):
        return

    print(name[index])
    print_recur(name, index + 1)


if __name__ == "__main__":
    print_recur("Priyanshu", 0)
    print_n_times(1, 10)
