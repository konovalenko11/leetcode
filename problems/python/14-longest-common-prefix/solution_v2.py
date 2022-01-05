import dis
from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    first_word = strs[0]

    for i in range(len(first_word)):
      letter = first_word[i]
      for s in strs[1:]:
        if i >= len(s) or letter != s[i]:
          return first_word[:i]

    return first_word

f = Solution()

strs = ["flower","flow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

strs = ["flower","xxlow","flight"]
print(f'Input: strs = {strs}')
print(f'Answer: {f.longestCommonPrefix(strs)}')

# dis.dis(f.addBinary)