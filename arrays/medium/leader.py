# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.


from sys import maxsize


def leader(nums):
    max_leader = -maxsize
    leaders = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > max_leader:
            max_leader = nums[i]
            leaders.insert(0, max_leader)
    return leaders


if __name__ == "__main__":
    print(leader([10, 22, 12, 3, 0, 6]))
