import dis
from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    result = [1]
    factorials = [0, 1]

    for i in range(2, rowIndex + 1):
      factorials.append(factorials[i-1] * i)

    for i in range(1, rowIndex):
      result.append(
        factorials[rowIndex] // (factorials[i] * factorials[rowIndex - i])
      )
      
    if rowIndex > 0:
      result.append(1)
      
    return result

f = Solution()

inputs = [ 
  {
    'rowIndex': 10
  }
]

for input in inputs:
  print(f'Input: {input}')
  print(f'Answer: {f.getRow(**input)}')