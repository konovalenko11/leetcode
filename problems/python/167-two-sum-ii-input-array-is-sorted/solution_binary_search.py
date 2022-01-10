from typing import Counter, List
import dis

def _adjust_boundary(etalon, start, stop, array, target):
  while (start < stop):
    mid = (start + stop) // 2
    sum = etalon + array[mid]

    if sum == target:
      return mid
    elif sum > target:
      stop = mid - 1
    else:
      start = mid + 1

  return start

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    for _ in range(len(numbers)):
      sum_left_right = numbers[left] + numbers[right]

      if sum_left_right == target:
        return [left + 1, right + 1]
      elif sum_left_right > target:
        right = _adjust_boundary(numbers[left], left, right - 1, numbers, 
                                 target)
      else:
        left = _adjust_boundary(numbers[right], left + 1, right, numbers, 
                                target)
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

numbers = [0,2,4,5,5,7,8,9,9,24]
target = 15
print(f'Input: numbers = {numbers}, target = {target}')
print(f'Answer: {f.twoSum(numbers, target)}')

numbers = [0,1,1,1,4,8,9,9,15,15]
target = 12
print(f'Input: numbers = {numbers}, target = {target}')
print(f'Answer: {f.twoSum(numbers, target)}')

numbers = [12, 13, 23, 28, 43, 44, 59, 60, 61, 68, 70, 86, 88, 92, 124, 125, 136, 168, 173, 173,
           180, 199, 212,
           221, 227, 230, 277, 282, 306, 314, 316, 321, 325, 328, 336, 337, 363, 365, 368, 370, 370, 371, 375,
           384, 387, 394, 400, 404, 414, 422, 422, 427, 430, 435, 457, 493, 506, 527, 531, 538, 541, 546, 568,
           583, 585, 587, 650, 652, 677, 691, 730, 737, 740, 751, 755, 764, 778, 783, 785, 789, 794, 803, 809,
           815, 847, 858, 863, 863, 874, 887, 896, 916, 920, 926, 927, 930, 933, 957, 981, 997]
target = 542
print(f'Input: numbers = {numbers}, target = {target}')
print(f'Answer: {f.twoSum(numbers, target)}')



# dis.dis(f.arrayPairSum)