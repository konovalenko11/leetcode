import dis
from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)

    # This will decrease the number of steps if it is higher than number of 
    # elements.
    k %= n

    anchor = 0
    content = 0

    for moved in range(n - 1):
      # This will properly calculate the new position, even if k < 0.
      content = (content + k + n) % n

      # If step is proportional to the length of the input array, we will 
      # eventually return to the anchor. In order to proceed with other numbers, 
      # we need to shift the anchor and try once more.
      if content == anchor:
        anchor += 1
        content = anchor
      else:
        # Swapping two numbers.
        nums[anchor], nums[content] = nums[content], nums[anchor]

      print(f'[{moved}]: [{anchor}] <=> [{content}]: {nums}; ')

f = Solution()

inputs = [ 
  {
    'nums': [1,2,3,4,5,6,7],
    'k': 3
  }, 
  {
    'nums': [1,2,3,4,5,6,7,8],
    'k': 4
  }, 
  {
    'nums': [1,2,3,4,5,6,7,8],
    'k': -2
  }, 
  {
    'nums': [-1,-100,3,99],
    'k': 2
  }
]

for input in inputs:
  print(f'Input: {input}')
  f.rotate(**input)
  print(f'Answer: {input}')