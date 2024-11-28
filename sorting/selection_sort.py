from typing import List


def selection_sort(nums: List[int]):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = (
            nums[min_index],
            nums[i],
        )

        print(
            f"After pass {i+1}, the sorted array is: {nums}"
        )  # print sorted array after each


if __name__ == "__main__":
    selection_sort([7, 8, 9, 2, 3, 1, 4])
