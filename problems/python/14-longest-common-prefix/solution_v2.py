import dis
from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = []
    first_word = strs[0]

    for i in range(len(first_word)):
      letter = first_word[i]
      for s in strs[1:]:
        if i >= len(s) or letter != s[i]:
          return ''.join(prefix)
      
      prefix.append(letter)

    return ''.join(prefix)

f = Solution()

strs = ["flower","flow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

strs = ["flower","xxlow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

# dis.dis(f.addBinary)