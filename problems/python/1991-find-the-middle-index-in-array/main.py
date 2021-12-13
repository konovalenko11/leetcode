''' 1991. Find the Middle Index in Array (Easy)
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if 
middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is 
no such index.
'''

from typing import List

class Solution:
  def find_middle_index(self, nums: List[int]) -> int:
    sum_before = 0
    sum_after = 0

    for num in nums:
      sum_after += num

    for i, num in enumerate(nums):
      sum_after -= num

      if sum_before == sum_after:
        return i

      sum_before += num

    return -1

f = Solution()

nums = [2,3,-1,8,4]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_middle_index(nums)}]')

nums = [1, 2, 3, 4, -5, 5, 5, 0]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_middle_index(nums)}]')

nums = [20, -10, 5, 5]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_middle_index(nums)}]')

nums = [1,7,3,6,5,6]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_middle_index(nums)}]')

nums = [1,2,3]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_middle_index(nums)}]')

nums = [2,1,-1]
print(f'Input array: {nums}')
print(f'Answer: [{f.find_middle_index(nums)}]')