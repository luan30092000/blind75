import pdb
from typing import List
from collections import defaultdict
import re           # isPalindrome: removing non-alphanumeric characters
class Solution:

    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
        it reads the same forward and backward. Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.

        

        Example 1:

        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.
        Example 2:

        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.
        Example 3:

        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.
        

        Constraints:

        1 <= s.length <= 2 * 105
        s consists only of printable ASCII characters.
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        s_len = len(s)
        for i in range(s_len):
            if s[i] != s[s_len - i - 1]:
                return False
            if i == s_len - i - 1:
                break
        return True
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        15. 3Sum
        
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.

        
        Example 1:

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
        
        
        Example 2:

        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.
        
        
        Example 3:

        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.


        Constraints:

        3 <= nums.length <= 3000
        -105 <= nums[i] <= 105
        """
        nums_dict = defaultdict(lambda: 0)
        for num in nums:
            nums_dict[num] += 1
        nums_len = len(nums)
        result =  []
        for i in range(nums_len):
            pdb.set_trace()
            if nums_dict[nums[i]] <= 0: continue
            j = i + 1
            while (j < nums_len):
                if nums_dict[nums[j]] <= 0:
                    j += 1
                    continue
                compl = 0 - (nums[i] + nums[j])
                if compl in nums_dict:
                    nums_dict[nums[i]] -= 1
                    nums_dict[nums[j]] -= 1
                    if nums_dict[compl] > 0:
                        result.append([nums[i],nums[j],compl])
                        nums_dict[compl] -= 1
                j += 1
        return result 
            

        