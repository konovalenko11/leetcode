import dis
from typing import List, Any, Tuple

def _parseExpression(s: str, cursor: int) -> Tuple:
  repeat_digits = []
  characters = []
  i = cursor

  while (i < len(s)):
    if s[i].isdigit():
      repeat_digits.append(s[i])
      i += 1
      continue

    if s[i] == '[':
      repeat = int(''.join(repeat_digits)) if repeat_digits else 1
      repeat_digits = []
      substr, i = _parseExpression(s, i+1)
      characters.append(substr * repeat)
      continue
    elif s[i] == ']':
      return (''.join(characters), i+1)
    else:
      characters.append(s[i])

    i += 1
    
  return (''.join(characters), i+1)
    
class Solution:
  def decodeString(self, s: str) -> str:
    return _parseExpression(s, 0)[0]

f = Solution()

inputs = [ 
  {
    's': '3[a]2[bc]'
  }, 
  {
    's': '3[a2[cd]]2[bc]'
  },
  {
    's': '2[abc]3[cd]ef'
  },
]

for input in inputs:
  print(f'Input: {input}')
  print(f'Answer: {f.decodeString(**input)}')
