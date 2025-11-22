# Problem Statement: Write a function to find the longest common prefix string amongst an array of strings. 
# If there is no common prefix, return an empty string "".
class Solution:  
    def longestCommonPrefix(self, st):
        if len(st) == 1:
            return st[0]
        elif len(st) == 0:
            return ""
        st = sorted(st)
        first_str = st[0]
        last_str = st[-1]
        j = -1
        i = 0
        while i < len(first_str) and i < len(last_str):
            if first_str[i] == last_str[i]:
                j = i
            else:
                break
            i += 1

        if j != -1:
            return first_str[0:j+1]    
        else:
            return ""