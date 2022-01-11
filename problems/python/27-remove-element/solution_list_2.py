from typing import List
import dis

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    forward = 0
    back = len(nums)

    while (forward < back):
      if nums[forward] == val:
        nums[forward] = nums[back - 1]
        back -= 1
      else:
        forward += 1
    return back

f = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
val = 1
print(f'Input: nums = {nums}, val = {val}')
print(f'Answer: {f.removeElement(nums, val)}')
print(f'Output list: nums = {nums}')

nums = [3,2,2,3]
val = 3
print(f'Input: nums = {nums}, val = {val}')
print(f'Answer: {f.removeElement(nums, val)}')
print(f'Output list: nums = {nums}')