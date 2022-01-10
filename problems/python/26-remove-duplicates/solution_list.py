from typing import List
import dis

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    
    last_num_idx = 0

    for i in range(1, len(nums)):
      if nums[i] != nums[last_num_idx]:
        last_num_idx += 1
        nums[last_num_idx] = nums[i]
    return last_num_idx + 1

f = Solution()

numbers = [0,0,1,1,1,2,2,3,3,4]
print(f'Input: numbers = {numbers}')
print(f'Answer: {f.removeDuplicates(numbers)}')
print(f'Output list: numbers = {numbers}')

# numbers = [2,3,4]
# target = 6
# print(f'Input: numbers = {numbers}, target = {target}')
# print(f'Answer: {f.twoSum(numbers, target)}')