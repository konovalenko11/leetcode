from typing import List
import dis

class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    start = 0
    end = 0
    ilength = 1
    isum = nums[0]
    # Choosing impossible value to have easier min comparison and to identify at 
    # the end if we haven't found any satisfying intervals.
    min_length = len(nums) + 1

    for end, num in enumerate(nums):
      isum += num
      ilength += 1

      while isum >= target:
        # Interval with length == 1 is the minimal possible interval.
        if ilength == 1:
          return ilength
        elif ilength < min_length:
          min_length = ilength

        isum -= nums[start]
        start += 1
        ilength -= 1

      print(f'interval[{start},{end}]; len[{ilength}]; sum[{isum}]')

    if min_length == len(nums) + 1:
      min_length = 0

    return min_length

f = Solution()

input = {
  'target': 7, 
  'nums': [2,3,1,2,4,3]
}

print(f'Input: {input}')
print(f'Answer: {f.minSubArrayLen(**input)}')

input = {
  'target': 70, 
  'nums': [2,3,1,2,4,3]
}

print(f'Input: {input}')
print(f'Answer: {f.minSubArrayLen(**input)}')

input = {
  'target': 7, 
  'nums': [2,3,7,2,4,3]
}

print(f'Input: {input}')
print(f'Answer: {f.minSubArrayLen(**input)}')

input = {
  'target': 7, 
  'nums': [7,3,7,2,4,3]
}

print(f'Input: {input}')
print(f'Answer: {f.minSubArrayLen(**input)}')