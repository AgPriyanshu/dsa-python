# Problem: Find the duplicate in an array of N+1 integers.
def find_dup(nums):
    for num in nums:
        index = abs(num)
        if nums[index] < 0:
            return index

        nums[index] = -nums[index]


if __name__ == "__main__":
    print(find_dup([3, 1, 3, 4, 2]))
