import dis
from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    triangle = []
    for r in range(rowIndex + 1):
      triangle.append([])

      for i in range(r + 1):
        if i == 0 or i == r:
          triangle[r].append(1)
        else:
          triangle[r].append(triangle[r-1][i-1] + triangle[r-1][i])

      print(f'[{r}]; triangle: {triangle}')
          
    return triangle[-1]

f = Solution()

inputs = [ 
  {
    'rowIndex': 3
  }
]

for input in inputs:
  print(f'Input: {input}')
  print(f'Answer: {f.getRow(**input)}')