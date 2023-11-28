import unittest
from b_two_pointers import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_two_pointers(self):
        self.assertEqual(self.solution.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(self.solution.isPalindrome("race a car"), False)
        self.assertEqual(self.solution.isPalindrome("race car"), True)
        self.assertEqual(self.solution.isPalindrome(" "), True)
        self.assertEqual(self.solution.isPalindrome("aaa"), True)
        self.assertEqual(self.solution.isPalindrome("bbbb"), True)

    def test_arrays_hashing(self):
        self.assertEqual(self.solution.threeSum([0,0,0,0]), [[0,0,0]])
        self.assertEqual(sorted(self.solution.threeSum([-1,0,1,2,-1,-4])), sorted([[-1,-1,2],[-1,0,1]]))
        self.assertEqual(self.solution.threeSum([0,1,1]),[])
        self.assertEqual(self.solution.threeSum([0,0,0]),[[0,0,0]])
if __name__ == '__main__':
    unittest.main()