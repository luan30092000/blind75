import unittest
from binary_search import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_binary_search(self):
        self.assertEqual(self.solution.findMin([4,5,0,1,2,3]), 0)
        self.assertEqual(self.solution.findMin([3,4,5,0,1,2]), 0)
        self.assertEqual(self.solution.findMin([2,3,4,5,0,1]), 0)
        self.assertEqual(self.solution.findMin([1,2,3,4,5,0]), 0)
        self.assertEqual(self.solution.findMin([0,1,2,3,4,5]), 0)
        self.assertEqual(self.solution.findMin([5,0,1,2,3,4]), 0)    
if __name__ == '__main__':
    unittest.main()