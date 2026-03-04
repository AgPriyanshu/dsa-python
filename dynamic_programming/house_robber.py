# A thief needs to rob money in a street. The houses in the street are arranged in a circular manner.
# Therefore the first and the last house are adjacent to each other. The security system in the street is
# such that if adjacent houses are robbed, the police will get notified.

# Given an array of integers “Arr'' which represents money at each house, we need to return the maximum
# amount of money that the thief can rob without alerting the police.


def house_robber(arr, n, dp):
    if n < 0:
        return 0
    if n == 0:
        return arr[n]
    if dp.get(n) is not None:
        return dp[n]
    pick = arr[n] + house_robber(arr, n - 2, dp)
    notPick = 0 + house_robber(arr, n - 1, dp)
    dp[n] = max(pick, notPick)
    return dp[n]

def house_robber_table(arr, n):
    if n < 0:
        return 0
    prev1, prev2 = arr[0],0
    for i in range(1,n):
        pick = arr[i] + (prev2 if i-2 >= 0 else 0)
        not_pick = prev1
        current = max(pick,not_pick)
        prev2 =prev1
        prev1=current

    return prev1


if __name__ == "__main__":
    arr = [1, 2]
    print(
        max(
            house_robber_table(arr[0 : len(arr) - 1], len(arr) - 2),
            house_robber_table(arr[1:], len(arr) - 2),
        )
    )
