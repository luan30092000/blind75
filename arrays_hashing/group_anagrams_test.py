import unittest
from group_anagrams import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_groupAnagrams(self):
        self.assertEqual(self.solution.groupAnagrams(sorted(["eat","tea","tan","ate","nat","bat"])), sorted([["bat"],["nat","tan"],["ate","eat","tea"]]))
        self.assertEqual(self.solution.groupAnagrams([""]), [[""]])
        self.assertEqual(self.solution.groupAnagrams(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()