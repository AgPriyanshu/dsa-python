# Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
# Note: Start the array with positive elements.

from typing import List


def rearrange_by_sign(arr: List[int]) -> List[int]:
    i = 0
    j = 1
    n = len(arr)
    result = [0] * n
    print(result)
    for num in arr:
        print(result)
        if num >= 0 and i < n:
            result[i] = num
            i += 2
        else:
            if j < n:
                result[j] = num
                j += 2
    return result


# Test the function
A = [1, 2, -3, -1, -2, 3]
ans = rearrange_by_sign(A)
print(ans)
