from typing import List

class Solution:
  def dominant_index(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return 0

    for i, num in enumerate(nums):
      if i == 0:
        max_value = num
        max_value_index = i
      elif num > max_value:
        second_max_value = max_value
        max_value = num
        max_value_index = i
      elif i == 1 or num > second_max_value:
        second_max_value = num

    if second_max_value == 0 or (max_value / second_max_value) >= 2:
      return max_value_index

    return -1

f = Solution()

nums = [3,6,1,0]
print(f'Input array: {nums}')
print(f'Answer: [{f.dominant_index(nums)}]')

nums = [3]
print(f'Input array: {nums}')
print(f'Answer: [{f.dominant_index(nums)}]')

nums = [0,0,0,1]
print(f'Input array: {nums}')
print(f'Answer: [{f.dominant_index(nums)}]')


