from typing import List
import dis

class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()

    sum = 0

    for i in range(0, len(nums), 2):
      sum += nums[i]
    
    return sum

f = Solution()

nums = [1,4,3,2]
print(f'Input: {nums}')
print(f'Answer: {f.arrayPairSum(nums)}')

nums = [6,2,6,5,1,2]
print(f'Input: {nums}')
print(f'Answer: {f.arrayPairSum(nums)}')

# dis.dis(f.arrayPairSum)