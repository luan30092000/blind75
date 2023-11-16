from typing import List
from collections import defaultdict 
import pdb
class Solution:
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
    """
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        O(n) time complexity
        O(n) space complexity
        """
        word_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            word_dict[sorted_word].append(word)
        
        return list(word_dict.values())