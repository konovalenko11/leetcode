import dis
    
class Solution:
  def decodeString(self, s: str) -> str:
    result_string = []
    repeat = 0
    stack = []

    for c in s:
      if c.isdigit():
        repeat = repeat * 10 + int(c)
      elif c == '[':
        stack.append((repeat, ''.join(result_string)))
        repeat = 0
        result_string = []
      elif c == ']':
        repetitions, last_value = stack.pop()
        result_string = [last_value + repetitions * ''.join(result_string)]
      else:
        result_string.append(c)
      
    return ''.join(result_string)

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
