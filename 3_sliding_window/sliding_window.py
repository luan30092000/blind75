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

        for i, char in enumerate(s):
            if char in aDict:
                temp = max(aDict[char], temp)
            result = max(result, i - temp + 1)
            aDict[char] = i + 1

        return result 
    
    def characterReplacement(self, s:str, k: int) -> int:
        """
        424. Longest Repeating Character Replacement

        You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
        Return the length of the longest substring containing the same letter you can get after performing the above operations. 

        ===> Algorithm note: Check if window_len = 1 work?. If yes: increase window len, else shift window right.

        Example 1:
        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.

        Example 2:
        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has the longest repeating letters, which is 4.
        There may exists other ways to achieve this answer too.
        
        Constraints:
        1 <= s.length <= 105
        s consists of only uppercase English letters.
        0 <= k <= s.length
        """
        window_len = 1
        start_i = 0
        while start_i + window_len < len(s):
            # Check if window_len = 1 work?
            if self.check_window(s, start_i, window_len, k):
                result = window_len
                window_len += 1
            else:
                start_i += 1