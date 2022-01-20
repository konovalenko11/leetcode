import dis
from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    result = [1]

    for i in range(1, rowIndex):
      result.append(
        result[i-1] * (rowIndex - i + 1) // i
      )
      
    if rowIndex > 0:
      result.append(1)

    return result

f = Solution()

inputs = [ 
  {
    'rowIndex': 300
  }
]

for input in inputs:
  print(f'Input: {input}')
  print(f'Answer: {f.getRow(**input)}')