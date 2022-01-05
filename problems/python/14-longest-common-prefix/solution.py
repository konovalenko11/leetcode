import dis
from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]

    for str in strs[1:]:
      for i in range(len(prefix)):
        if i >= len(str) or prefix[i] != str[i]:
          prefix = prefix[:i]
          break
      
      if not prefix:
        break

    return prefix

f = Solution()

strs = ["flower","flow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

strs = ["flower","xxlow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

# dis.dis(f.addBinary)