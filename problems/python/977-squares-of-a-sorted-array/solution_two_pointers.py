from typing import List
import dis
from collections import deque

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    squares = deque()
    left = 0
    right = len(nums) - 1

    while left < right:
      if abs(nums[right]) > abs(nums[left]):
        squares.appendleft(nums[right]**2)
        right -= 1
      else:
        squares.appendleft(nums[left]**2)
        left += 1

    squares.appendleft(nums[left]**2)

    return list(squares)

f = Solution()

input = {
  'nums': [-4,-1,0,3,10]
}

print(f'Input: {input}')
print(f'Answer: {f.sortedSquares(**input)}')