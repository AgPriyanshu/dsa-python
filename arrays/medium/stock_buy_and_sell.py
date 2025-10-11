# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from math import floor
from typing import List
import sys


def stock_buy_and_sell(nums: List[int]):
    min = sys.maxsize
    max = -sys.maxsize - 1
    for num in nums:
        if num <= min:
            min = num
        if num - min > max:
            max = num - min
    return max


if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]
    print(stock_buy_and_sell(nums))
