from typing import List

class Solution:
  def find_pivot_index(self, nums: List[int]) -> int:
    sum_before = 0
    total_sum = sum(nums)

    for i, num in enumerate(nums):
      if sum_before == (total_sum - num - sum_before):
        return i

      sum_before += num

    return -1

f = Solution()

nums = [2,3,-1,8,4]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_pivot_index(nums)}]')

nums = [1, 2, 3, 4, -5, 5, 5, 0]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_pivot_index(nums)}]')

nums = [20, -10, 5, 5]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_pivot_index(nums)}]')

nums = [1,7,3,6,5,6]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_pivot_index(nums)}]')

nums = [1,2,3]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_pivot_index(nums)}]')

nums = [2,1,-1]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_pivot_index(nums)}]')