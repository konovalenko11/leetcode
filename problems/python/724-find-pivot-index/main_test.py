import inspect
import os
import sys
import unittest

# Dynamically importing current directory modules
filename = inspect.getframeinfo(inspect.currentframe()).filename
sys.path.insert(0, os.path.dirname(os.path.abspath(filename)))
import main_2 as solution
from parameterized import parameterized


class TestSolution(unittest.TestCase):

  @classmethod
  def setUpClass(cls) -> None:
    cls.solution = solution.Solution()

  @parameterized.expand([
    ([2,3,-1,8,4], -1),
    ([1, 2, 3, 4, -5, 5, 5, 0], -1),
    ([20, -10, 5, 5], -1),
    ([1,7,3,6,5,6], -1),
    ([1,2,3], -1),
    ([2,1,-1], -1),
  ])
  def test_find_pivot_index(self, input, expected):
    self.assertEqual(self.solution.find_pivot_index(input), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
