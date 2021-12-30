from typing import List
import dis

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    result_list = [[1]]

    for rownum in range(1, numRows):
      result_list.append([1])
      for elnum in range(1, rownum + 1):
        if elnum == rownum:
          result_list[rownum].append(1)
        else:
          result_list[rownum].append(
            result_list[rownum - 1][elnum - 1] + 
            result_list[rownum - 1][elnum]
          )
    return result_list

f = Solution()

numRows = 5
print(f'numRows: {numRows}')
print(f'Answer: {f.generate(numRows)}')

numRows = 1
print(f'numRows: {numRows}')
print(f'Answer: {f.generate(numRows)}')

numRows = 10
print(f'numRows: {numRows}')
print(f'Answer: {f.generate(numRows)}')

# dis.dis(f.generate)