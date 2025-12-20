# Problem: Contains Duplicate : Check if a value appears atleast twice
from typing import List


def contains_duplicate(nums: List[int]):
    map = {}
    for i in nums:
        if map.get(i) is not None:
            return True
        else:
            map[i] = 1

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(contains_duplicate(nums))
