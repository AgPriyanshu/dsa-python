from copy import copy

results = []


def backtrack(nums, string_list=""):
    results.append(string_list)
    if len(nums) == 0:
        return
    print(string_list, nums)
    for index, num in enumerate(nums):
        # if index <= len(nums):
        temp = copy(nums)
        temp_string = copy(string_list)
        temp_string += str(num)
        temp.pop(index)
        # print(string_list)
        backtrack(temp, temp_string)


if __name__ == "__main__":
    backtrack([2, 3, 4, 5])
    print(results)
