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
        # nums_dict = defaultdict(lambda: 0)
        # for num in nums:
        #     nums_dict[num] += 1
        # nums_len = len(nums)
        # result =  []
        # for i in range(nums_len):
        #     pdb.set_trace()
        #     if nums_dict[nums[i]] <= 0: continue
        #     j = i + 1
        #     while (j < nums_len):
        #         if nums_dict[nums[j]] <= 0:
        #             j += 1
        #             continue
        #         compl = 0 - (nums[i] + nums[j])
        #         if compl in nums_dict:
        #             nums_dict[nums[i]] -= 1
        #             nums_dict[nums[j]] -= 1
        #             if nums_dict[compl] > 0:
        #                 result.append([nums[i],nums[j],compl])
        #                 nums_dict[compl] -= 1
        #         j += 1
        # return result 

        result = []
        nums.sort()
        nums_len = len(nums)
        
        for i, value in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:  
                continue
            j = i + 1
            k = nums_len - 1
            while j < k:
                threeSum = value + nums[j] + nums[k]
                if threeSum == 0: 
                    result.append([value, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif threeSum < 0:
                    j += 1
                else:
                    k -= 1
        return result
    def maxArea_bruteForce(self, height: List[int]) -> int:
        """
        Runtime: O(n^2)
        """
        result_maxVolume = 0
        for index1, height1 in enumerate(height):
            # Use this to traverse from a specific index but keep the origin indices values
            for index2, height2 in enumerate(height[index1:], index1):  
                temp_volume = (index2 - index1) * min(height[index1], height[index2])
                if result_maxVolume < temp_volume: result_maxVolume = temp_volume
        return result_maxVolume
    def maxArea(self, height: List[int]) -> int:
        """
        11. Contain with most water
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        Notice that you may not slant the container.

        Example 1:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

        Example 2:
        Input: height = [1,1]
        Output: 1

        Constraints:
        n == height.length
        2 <= n <= 105
        0 <= height[i] <= 104

        Runtime: O(n^2)
        """
        result = 0
        left = 0
        right = len(height) - 1
        while (right > left):
            temp = (-left + right) * min(height[right], height[left])
            if result < temp: result = temp
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return result 