import unittest
from sliding_window import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_maxProfit(self):
        self.assertEqual(self.solution.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(self.solution.maxProfit([7,6,4,3,1]), 0)
    
    def test_lengthOfLongestSubstring(self):
        test_cases = [("abcabcbb", 3), 
                      ("bbbbb", 1), 
                      ("pwwkew", 3), 
                      (" ", 1), 
                      ("abcdba", 4)]
        for i, (s, expected) in enumerate(test_cases):
            try:
                self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
            except AssertionError as e:
                print(f"Test case {i+1} failed: {e}")
if __name__ == '__main__':
    unittest.main()