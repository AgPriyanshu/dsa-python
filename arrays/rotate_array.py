def reverse(nums, start, end):
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# Reversal algorithm
def rotate_to_right(nums, d_places):
    n = len(nums)
    reverse(nums, 0, n - d_places - 1)
    reverse(nums, n - d_places, n - 1)
    reverse(nums, 0, n - 1)


def rotate_to_left(nums, d_places):
    n = len(nums)
    reverse(nums, 0, d_places - 1)
    reverse(nums, d_places, n - 1)
    reverse(nums, 0, n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 11
    # rotate_to_right(nums, 2)
    k = 11 % len(nums)
    rotate_to_left(nums, k)
    print(nums)
