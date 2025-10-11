# Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
# Note: Start the array with positive elements.

from typing import List


def RearrangebySign(A: List[int]) -> List[int]:
    n = len(A)

    # Define array for storing the ans separately.
    ans = [0] * n

    # positive elements start from 0 and negative from 1.
    posIndex, negIndex = 0, 1
    for i in range(n):

        # Fill negative elements in odd indices and inc by 2.
        if A[i] < 0:
            ans[negIndex] = A[i]
            negIndex += 2

        # Fill positive elements in even indices and inc by 2.
        else:
            ans[posIndex] = A[i]
            posIndex += 2

    return ans


# Test the function
A = [1, 2, -4, -5]
ans = RearrangebySign(A)
print(ans)
