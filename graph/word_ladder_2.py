# Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths. Find all shortest transformation sequence(s) from startWord to targetWord. You can return them in any order possible.


# In this problem statement, we need to keep the following conditions in mind:


# A word can only consist of lowercase characters.

# Only one letter can be changed in each transformation.

# Each transformed word must exist in the wordList including the targetWord.

# startWord may or may not be part of the wordList.

# Return an empty list if there is no such transformation sequence.

from collections import deque

class Solution:
    
    def findSequences(self, startWord, 
                        targetWord, wordList):

        q = deque([[startWord]])
        wordListSet = set(wordList)
        wordListSet.discard(startWord)
        ans = []
        while q:
            words_to_remove = set()
            for _ in range(len(q)):
                qList = q.popleft()
                latest_word = qList[-1]
                if latest_word == targetWord:
                    if not ans:
                        ans.append(qList)
                    elif len(ans[-1]) == len(qList):
                        ans.append(qList)               

                # Traverse the whole level.
                for i in range(len(latest_word)):
                    for ch in range(ord('a'),ord('z')+1):
                        word = latest_word[:i] + chr(ch) + latest_word[i+1:]
                        if word in wordListSet:
                            q.append([*qList,word])
                            words_to_remove.add(word)

            for removeWord in words_to_remove:
                wordListSet.remove(removeWord)
            if ans:
                break


        return ans

if __name__ == "__main__":
    startWord = "geek"
    targetWord = "gedk"
    wordList = ["geek", "gefk"]
    print(Solution().findSequences(startWord,targetWord,wordList))