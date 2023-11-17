import unittest
from arrays_hashing import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_groupAnagrams(self):
        self.assertEqual(self.solution.groupAnagrams(sorted(["eat","tea","tan","ate","nat","bat"])), sorted([["bat"],["nat","tan"],["ate","eat","tea"]]))
        self.assertEqual(self.solution.groupAnagrams([""]), [[""]])
        self.assertEqual(self.solution.groupAnagrams(["a"]), [["a"]])

    def test_topKFrequent(self):
        self.assertEqual(self.solution.topKFrequent(sorted([1,1,1,2,2,3]), 2), sorted([1,2]))
        self.assertEqual(self.solution.topKFrequent(sorted([1]), 1), sorted([1]))

    def test_productExceptSelf(self):
        self.assertEqual(self.solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(self.solution.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

if __name__ == '__main__':
    unittest.main()