from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    result_list = []

    for rownum in range(numRows):
      row_elements = []

      for elnum in range(rownum + 1):
        if elnum == 0 or elnum == rownum:
          row_elements.append(1)
        else:
          row_elements.append(
            result_list[rownum - 1][elnum - 1] + 
            result_list[rownum - 1][elnum]
          )

      result_list.append(row_elements)
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

# mat = [[2,5,8],[4,0,-1]]
# print(f'Input array: {mat}')
# print(f'Answer: {f.spiral_matrix(mat)}')

# mat = [[2,5],[4,0], [8,5], [4,3]]
# print(f'Input array: {mat}')
# print(f'Answer: {f.spiral_matrix(mat)}')

# mat = []
# print(f'Input array: {mat}')
# print(f'Answer: {f.spiral_matrix(mat)}')

# mat = [[]]
# print(f'Input array: {mat}')
# print(f'Answer: {f.spiral_matrix(mat)}')

# mat = [[1],[2], [3]]
# print(f'Input array: {mat}')
# print(f'Answer: {f.spiral_matrix(mat)}')

# mat = [[1, 2, 3]]
# print(f'Input array: {mat}')
# print(f'Answer: {f.spiral_matrix(mat)}')