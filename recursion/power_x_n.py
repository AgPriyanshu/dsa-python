def pow(x, n):
    if n == 0:
        return 1
    return x * pow(x, n - 1)
