from typing import List
import dis

class Solution:
  def addBinary(self, a: str, b: str) -> str:
    result = []
    extra_num = 0

    a_norm = '0' * (len(b) - len(a)) + a
    b_norm = '0' * (len(a) - len(b)) + b

    for i in range(len(a_norm) - 1, -1, -1):
      sum_num = int(a_norm[i]) + int(b_norm[i]) + extra_num

      result_num = sum_num % 2
      extra_num = sum_num // 2

      result.insert(0, str(result_num))
    
    if extra_num == 1:
      result.insert(0, str(extra_num))

    return ''.join(result)

f = Solution()

a = '11'
b = '1'
print(f'Input: a = "{a}", b = "{b}"')
print(f'Answer: {f.addBinary(a, b)}')

a = '1010'
b = '1011'
print(f'Input: a = "{a}", b = "{b}"')
print(f'Answer: {f.addBinary(a, b)}')

# dis.dis(f.addBinary)