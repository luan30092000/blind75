import unittest
from cmpt307 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_groupAnagrams(self):
        self.assertEqual(self.solution.lifeBoat([], 0), 0)
        self.assertEqual(self.solution.lifeBoat([2, 4, 7, 8, 10], 10), 4)
        self.assertEqual(self.solution.lifeBoat([2, 4, 6, 8, 10], 10), 3)
        self.assertEqual(self.solution.lifeBoat([1, 2, 4, 5, 6, 7, 8, 8, 9, 11], 10), 7)
        self.assertEqual(self.solution.lifeBoat([1, 12, 14, 15, 16, 17, 18, 18, 19, 11], 10), 10)
if __name__ == '__main__':
    unittest.main()