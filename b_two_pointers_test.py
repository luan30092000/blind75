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

if __name__ == '__main__':
    unittest.main()