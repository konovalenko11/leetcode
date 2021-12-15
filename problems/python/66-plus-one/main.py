from typing import List

class Solution:
  def plus_one(self, digits: List[int]) -> int:
    for i in range(len(digits) - 1, -1, -1):
      if digits[i] != 9:
        digits[i] += 1
        return digits
      else:
        digits[i] = 0

    return [1] + digits

f = Solution()

digits = [3,6,1,0]
print(f'Input array: {digits}')
print(f'Answer: [{f.plus_one(digits)}]')

digits = [9,9]
print(f'Input array: {digits}')
print(f'Answer: [{f.plus_one(digits)}]')