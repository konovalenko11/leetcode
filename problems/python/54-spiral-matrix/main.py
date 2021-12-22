from typing import List

class Solution:
  def spiral_matrix(self, mat: List[List[int]]) -> List[int]:
    # Output list.
    result_list = []

    # If list is empty.
    if not mat:
      return result_list

    # Rows, columns.
    nrows = len(mat)
    ncols = len(mat[0])
    nelements = nrows * ncols

    # if array is flat or empty, then there is not need to traverse the matrix 
    # by diagonal.
    if nrows < 2 or ncols < 2:
      for row in mat:
        for element in row:
          result_list.append(element)
      return result_list

    # Initial position.
    x = 0
    y = 0

    # Initial vector.
    xd = 0
    yd = 1

    # Lap counter.
    side_moves = 1
    side_moves_limit = ncols
    sides_passed = 0
    laps = 0

    # Adding initial point.
    result_list.append(mat[x][y])

    for _ in range(nelements-1):

      if side_moves == side_moves_limit:
        side_moves = 1
        sides_passed += 1
        laps = (sides_passed + 1) // 4

        if sides_passed % 2 == 0:
          side_moves_limit = ncols - laps
        else:
          side_moves_limit = nrows - laps

        # Rotating direction vector clockwise (x, y) -> (y, -x).
        xd, yd = yd, -xd

      x += xd
      y += yd

      result_list.append(mat[x][y])

      side_moves += 1

    return result_list

f = Solution()

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[2,5,8],[4,0,-1]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[2,5],[4,0], [8,5], [4,3]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = []
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[1],[2], [3]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[1, 2, 3]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')