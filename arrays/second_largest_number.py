from typing import List


def second_largest_and_smallest_element(nums: List[int]):
    max = nums[0]
    max_prev = nums[0]
    min = nums[0]
    min_prev = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max_prev = max
            max = nums[i]

        if nums[i] < min:
            min_prev = min
            min = nums[i]

    return (max_prev, max, min_prev, min)


if __name__ == "__main__":
    nums = [10, 5, 8, 2, 15, 7]
    number_tuple = second_largest_and_smallest_element(nums)
    print(number_tuple)
