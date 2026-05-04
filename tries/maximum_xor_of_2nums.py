# Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
# where 0 <= i <= j < n.

class Node:
    def __init__(self):
        # Each node has two possible children:
        # links[0] -> represents bit 0
        # links[1] -> represents bit 1
        self.links = [None, None]

class BitsTrie:
    def __init__(self):
        # Root of the Trie
        self.root = Node()

    def insert(self, num):
        """
        Insert a number into the Trie.
        We go from MSB (bit 31) to LSB (bit 0)
        so that numbers are aligned bit-by-bit.
        """
        node = self.root
        for i in range(31, -1, -1):
            # Extract i-th bit
            bit = (num >> i) & 1

            # If path for this bit doesn't exist, create it
            if not node.links[bit]:
                node.links[bit] = Node()

            # Move to the next node
            node = node.links[bit]

    def get_max_xor(self, num):
        """
        For a given number, try to find the number in Trie
        that gives maximum XOR with it.
        """
        node = self.root
        ans = 0

        for i in range(31, -1, -1):
            # Extract current bit
            bit = (num >> i) & 1

            # We want the opposite bit to maximize XOR
            toggled = 1 - bit  # (or bit ^ 1)

            # If opposite bit exists, take that path
            if node.links[toggled]:
                # Set the i-th bit in answer
                # because XOR at this position will be 1 be 2 different bits always give 1.
                ans |= (1 << i)

                # Move to that node
                node = node.links[toggled]
            else:
                # Otherwise, we have no choice but to take same bit path
                node = node.links[bit]

        return ans

class Solution:
    def findMaximumXOR(self, nums):
        # Build Trie with all numbers
        trie = BitsTrie()
        for num in nums:
            trie.insert(num)

        max_val = 0

        # For each number, find best XOR possible
        for num in nums:
            max_val = max(trie.get_max_xor(num), max_val)

        return max_val

if __name__ == "__main__":
    nums = [26, 49, 30, 15, 69]
    print(Solution().findMaximumXOR(nums))