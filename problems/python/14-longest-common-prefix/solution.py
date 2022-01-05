import dis
from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]

    for str in strs[1:]:
      new_prefix = []

      for i in range(len(prefix)):
        if i >= len(str) or prefix[i] != str[i]:
          break

        new_prefix.append(prefix[i])

      prefix = new_prefix.copy()
    return ''.join(prefix)

f = Solution()

strs = ["flower","flow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

strs = ["flower","xxlow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

# dis.dis(f.addBinary)