from typing import List
from collections import defaultdict, Counter
import pdb
import heapq
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        Example 1:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Example 2:
        Input: strs = [""]
        Output: [[""]]

        Example 3:
        Input: strs = ["a"]
        Output: [["a"]]

        Constraints:

        1 <= strs.length <= 104
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.
        
        O(n) time complexity
        O(n) space complexity
        """
        word_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            word_dict[sorted_word].append(word)
        
        return list(word_dict.values())

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
        Example 1:

        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        Example 2:

        Input: nums = [1], k = 1
        Output: [1]
        

        Constraints:

        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.

        O(nlogk) time complexity -> O(n) when k is small
        O(n) space complexity
        
        Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
        """
    
        dict_nums_counter = defaultdict(lambda: 0)  # return 0 if key not found in dict
        for num in nums:
            dict_nums_counter[num] += 1
        # OR 
        # dict_nums_counter = Counter(nums)


        # OR
        # result_list = sorted(dict_nums.items(), key=lambda x:x[1], reverse=True)  # Sort dict by value, return list type -> sort whole dict -> longer
        result_list = heapq.nlargest(k, dict_nums_counter.keys(), key = dict_nums_counter.get)      # Sort k largest element in dict
        return result_list