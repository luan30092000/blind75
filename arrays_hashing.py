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
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.

        Example 1:

        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]
        

        Constraints:

        2 <= nums.length <= 105
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        

        Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
        """
        # Common sense
        # length = len(nums)
        # mapRight = {}
        # mapLeft = {}
        # mapRight[length-1] = 1
        # mapLeft[0] = 1
        # for i in range(length):
        #     # pdb.set_trace()
        #     if length-i-1 not in mapRight:
        #         mapRight[length-i-1] = mapRight[length-i]*nums[length-i]
        #     if i not in mapLeft:
        #         mapLeft[i] = mapLeft[i-1]*nums[i-1]
        # result = []
        # # pdb.set_trace()
        # for i in range(length):
        #     result.append(mapRight[i] * mapLeft[i])
        # # pdb.set_trace()
        # return result;
        # Why did I even use hashhhh, this is crazyyyyyy. 
        
        length = len(nums)
        result = [1] * length

        left_product = 1
        for i in range(length):
            result[i] = left_product
            left_product *= nums[i]
            
        right_product = 1
        for i in reversed(range(length)):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
    
    def encode(self, strs: List[str]) -> str:
        """
        Encode a list of strings to a string
        @param: strs: a list of strings
        @return: a single encoded string
        """
        pass

    def decode(self, s: str) -> List[str]:
        """
        Decoded back to the original list of strings
        @param: s: a single string
        @return: original list of strings
        """
        pass

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

        Constraints:
        0 <= nums.length <= 105
        -109 <= nums[i] <= 109

        Runtime:
        O(n) run time complexity
        O(n) space complexity
        """
        length = len(nums)
        if (length == 0 or length == 1):
            return 0 if length == 0 else 1
        nums_set = set(nums)
        result = 1
        for num in nums:
            temp_result =1 
            if num - 1 not in nums_set:
                temp = num
                while temp + 1 in nums_set:
                    temp_result += 1 
                    temp += 1
                result = max(result, temp_result)
        return result;
            
                
        