def binary_search(nums: list[int], valueToFind: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == valueToFind:
            return mid
        elif nums[mid] < valueToFind:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    test_nums = [23, 3451, 1231, 544, 6, 78, 9]
    print(binary_search(test_nums, 6))
