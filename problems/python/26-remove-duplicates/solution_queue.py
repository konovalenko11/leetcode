from typing import List
import dis
from collections import deque

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    
    last_num = None
    gaps = deque()
    unique_nums_count = 0
    
    for i in range(len(nums)):
      if nums[i] == last_num:
        gaps.append(i)
        nums[i] = '_'
      else:
        last_num = nums[i]
        unique_nums_count += 1

        if gaps:
          gap_idx = gaps.popleft()
          nums[gap_idx], nums[i] = nums[i], nums[gap_idx]
          gaps.append(i)
    
    return unique_nums_count

f = Solution()

numbers = [0,0,1,1,1,2,2,3,3,4]
print(f'Input: numbers = {numbers}')
print(f'Answer: {f.removeDuplicates(numbers)}')
print(f'Output list: numbers = {numbers}')

# numbers = [2,3,4]
# target = 6
# print(f'Input: numbers = {numbers}, target = {target}')
# print(f'Answer: {f.twoSum(numbers, target)}')