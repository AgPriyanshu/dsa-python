# Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.
# Return the maximum score that can be obtained.

class Solution:
  def maxScore(self, cardScore, k):
    n = len(cardScore)
    sum_k = sum(cardScore[n - k:n])
    max_sum = sum_k
    for i in range(n,(n + k)):
      sum_k = sum_k - (cardScore[(i-k)%n]) + cardScore[i%n]
      max_sum = max(max_sum,sum_k)


    return max_sum

if __name__ == "__main__":
  cardScore = [5, 4, 1, 8, 7, 1, 3 ]
  k = 3
  print(Solution().maxScore(cardScore,k))