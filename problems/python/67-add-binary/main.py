from typing import List
import dis

class Solution:
  def addBinary(self, a: str, b: str) -> str:
    result = []
    extra_num = 0

    max_len = max(len(a), len(b))
    a_norm = a.zfill(max_len)
    b_norm = b.zfill(max_len)

    for i in range(max_len - 1, -1, -1):
      sum_num = int(a_norm[i]) + int(b_norm[i]) + extra_num

      result_num = sum_num % 2
      extra_num = sum_num // 2

      result.append(str(result_num))
    
    if extra_num == 1:
      result.append(str(extra_num))

    result.reverse()

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