from typing import List


def union(a1: List[int], a2: List[int]):
    n = len(a1)
    m = len(a2)
    i = 0
    j = 0
    new_arr = []
    while i < n and j < m:
        print(f"i: {i}, j: {j},a1[i]: {a1[i]}, a2[j]: {a2[j]},")
        element_to_add = a1[i]
        if a1[i] == a2[j]:
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            element_to_add = a2[j]
            j += 1
        new_arr.append(element_to_add)

    while i < n:
        new_arr.append(a1[i])
        i += 1
    while j < m:
        new_arr.append(a2[j])
        j += 1
    return new_arr


if __name__ == "__main__":
    a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a2 = [2, 3, 4, 4, 5, 11, 12]
    print(union(a1, a2))
