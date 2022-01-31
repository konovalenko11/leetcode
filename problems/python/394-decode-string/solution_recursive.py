import dis
    
class Solution:
  def __init__(self) -> None:
    self.cursor = 0

  def decodeString(self, s: str) -> str:
    repeat = 0
    characters = []

    while (self.cursor < len(s)):
      if s[self.cursor].isdigit():
        repeat = repeat * 10 + int(s[self.cursor])
      elif s[self.cursor] == '[':
        self.cursor += 1
        substr = self.decodeString(s)
        characters.append(substr * repeat)
        repeat = 0
        continue
      elif s[self.cursor] == ']':
        self.cursor += 1
        return ''.join(characters)
      else:
        characters.append(s[self.cursor])

      self.cursor += 1

    self.cursor += 1
      
    return ''.join(characters)

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
  f.cursor = 0
  print(f'Answer: {f.decodeString(**input)}')
