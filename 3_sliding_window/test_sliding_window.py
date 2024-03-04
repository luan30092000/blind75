import unittest
from sliding_window import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_maxProfit(self):
        self.assertEqual(self.solution.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(self.solution.maxProfit([7,6,4,3,1]), 0)
    
    def test_lengthOfLongestSubstring(self):
        # self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        # self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        # self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring(" "), 1)
if __name__ == '__main__':
    unittest.main()