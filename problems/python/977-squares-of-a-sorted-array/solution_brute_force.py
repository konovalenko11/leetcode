from typing import List
import dis

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    negatives = []
    squares = []

    for i, num in enumerate(nums):
      if num < 0:
        negatives.append(abs(num))
        continue
      
      while negatives and negatives[-1] < num:
        squares.append(negatives.pop()**2)
      
      squares.append(num**2)

    while negatives:
      squares.append(negatives.pop()**2)

    return squares

f = Solution()

input = {
  'nums': [-4,-1,0,3,10]
}

print(f'Input: {input}')
print(f'Answer: {f.sortedSquares(**input)}')