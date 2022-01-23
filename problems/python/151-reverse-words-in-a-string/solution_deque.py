import dis
from typing import List
from collections import deque

class Solution:
  def reverseWords(self, s: str) -> str:
    result_words = deque()
    word_chars = []

    for c in s:
      if not c.isspace():
        word_chars.append(c)
      elif word_chars:
        result_words.appendleft(''.join(word_chars))
        word_chars = []

    if word_chars:
      result_words.appendleft(''.join(word_chars))

    return ' '.join(result_words)

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