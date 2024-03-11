from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        121. Best Time to Buy and Sell Stock
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        

        Example 1:

        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
        Example 2:

        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.
        

        Constraints:

        1 <= prices.length <= 105
        0 <= prices[i] <= 104

        Runtime: O(n)
        """
        left = 0
        right = 1 
        result = 0
        while(right < len(prices)):
            if prices[right] > prices[left]:
                temp = prices[right] - prices[left]
                if (result < temp): result = temp
                right += 1
            elif prices[right] <= prices[left]:
                left = right
                right = left + 1
        return result   
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters
        Given a string s, find the length of the longest substring without repeating characters.

        
        Example 1:

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        Example 2:

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        Example 3:

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        

        Constraints:

        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces. 
        """
        result = 0
        aDict = {}
        temp = 0
        for i, c in enumerate(s):
            if c in aDict:
                temp = max(aDict[c], temp)
            result = max(result, i - temp + 1)
            aDict[c] = i + 1
        return result