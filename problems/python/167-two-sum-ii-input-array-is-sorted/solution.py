from typing import List
import dis

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:

    i = 0
    j = len(numbers) - 1

    for _ in range(len(numbers)):
      sum = numbers[i] + numbers[j]

      if sum > target:
        j -= 1
      elif sum < target:
        i += 1
      else:
        return [i+1, j+1]

    return [1, 2]

f = Solution()

numbers = [2,7,11,15]
target = 9
print(f'Input: numbers = {numbers}, target = {target}')
print(f'Answer: {f.twoSum(numbers, target)}')

numbers = [2,3,4]
target = 6
print(f'Input: numbers = {numbers}, target = {target}')
print(f'Answer: {f.twoSum(numbers, target)}')

# dis.dis(f.arrayPairSum)