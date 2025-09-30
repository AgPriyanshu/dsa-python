# Problem Statement: Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair.
# At a time we can climb either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.


def climbing_stairs(current):
    if current <= 1:
        return 1
    else:
        return climbing_stairs(current - 1) + climbing_stairs(current - 2)


if __name__ == "__main__":
    print(climbing_stairs(3))
