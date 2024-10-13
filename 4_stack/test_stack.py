import unittest
from stack import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_isValid(self):
        self.assertEqual(self.solution.isValid("()"), True)
        self.assertEqual(self.solution.isValid("()[]{}"), True)
        self.assertEqual(self.solution.isValid("(]"), False)
        self.assertEqual(self.solution.isValid("([)]"), False)
        self.assertEqual(self.solution.isValid("([])"), True)
    
if __name__ == '__main__':
    unittest.main()