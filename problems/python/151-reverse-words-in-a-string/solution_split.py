import dis
from typing import List

class Solution:
  def reverseWords(self, s: str) -> str:
    return ' '.join([k for k in s.strip().split(' ')[::-1] if k])

f = Solution()

inputs = [ 
  {
    's': "the sky is blue"
  },
  {
    's': "  hello world  "
  },
]

for input in inputs:
  print(f'Input: {input}')
  print(f'Answer: [{f.reverseWords(**input)}]')