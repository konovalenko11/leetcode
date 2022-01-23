import dis
from typing import List
from collections import deque

class Solution:
  def reverseWords(self, s: str) -> str:
    # Emulating immutability
    s = list(s)

    if 



    return ''

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