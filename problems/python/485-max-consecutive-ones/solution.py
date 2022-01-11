from typing import List
import dis

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    max_rep = 0
    curr_rep = 0

    for num in nums:
      if num == 1:
        curr_rep += 1
      else:
        if curr_rep > max_rep:
          max_rep = curr_rep
        curr_rep = 0

    return max(max_rep, curr_rep)

f = Solution()

input = {
  'nums': [1,1,0,1,1,1]
}

print(f'Input: {input}')
print(f'Answer: {f.findMaxConsecutiveOnes(**input)}')
