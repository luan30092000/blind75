import unittest
from binary_search import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_binary_search_find_min(self):
        self.assertEqual(self.solution.findMin([4,5,0,1,2,3]), 0)
        self.assertEqual(self.solution.findMin([3,4,5,0,1,2]), 0)
        self.assertEqual(self.solution.findMin([2,3,4,5,0,1]), 0)
        self.assertEqual(self.solution.findMin([1,2,3,4,5,0]), 0)
        self.assertEqual(self.solution.findMin([0,1,2,3,4,5]), 0)
        self.assertEqual(self.solution.findMin([5,0,1,2,3,4]), 0)    

    def test_binary_search_search(self):
        self.assertEqual(self.solution.search([0], 0), 0)
        self.assertEqual(self.solution.search([1], 1), 0)
        self.assertEqual(self.solution.search([1,3], 1), 0)
        self.assertEqual(self.solution.search([3,1], 1), 1)
        self.assertEqual(self.solution.search([1,2,3], 1), 0)
        self.assertEqual(self.solution.search([3,1,2], 1), 1)
        self.assertEqual(self.solution.search([2,3,1], 1), 2)

if __name__ == '__main__':
    unittest.main()