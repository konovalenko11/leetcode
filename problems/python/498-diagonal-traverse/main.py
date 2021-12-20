from typing import List

class Solution:
  def diagonal_traverse(self, mat: List[List[int]]) -> List[int]:
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
    y = 1

    # There are only couple of options where we can move:
    #  - main directions: down-left, up-right;
    #  - alternative directions (if we come to matrix boundaries): down, right.
    # There is also a nuance if we get to the matrix boundary. If direction is 
    # down-left, then we need to try alternative routes counter-clockwise: first 
    # down, then right. If direction is up-right, then we need to check alternative routes clockwise:
    # first right, then down.

    # Initial set of moves (vectors) by X (rows) and Y (columns):
    #  - default vector: [1, -1] (down, left)
    #  - alternative 1: [1, 0] (down)
    #  - alternative 2: [0, 1] (right)
    vectors = [[1, -1], [1, 0], [0, 1]]
    change_direction = False

    # To simpify the logic we want to exclude first and last elements from the 
    # traversing as they are known to be at the beginning and at the end of the 
    # result list. So the starting (initial) point will be (0, 1).
    # Including it into the result array as well together with the (0, 0).
    result_list = [mat[0][0], mat[x][y]] 

    # We expect n-3 transitions as first, second, and last points are known.
    for _ in range(nelements - 3):
      for vector in vectors:
        xnew = x + vector[0]
        ynew = y + vector[1]

        # Defining coordinates. If new coordinate is within the matrix, then 
        # assigning it. Otherwise (if we came to the box edge), we need to change 
        # the direction and move vertically: x = x + 1, ynew = y.
        if (xnew >= 0 and xnew < nrows) and (ynew >= 0 and ynew < ncols):
          x = xnew
          y = ynew
          break
        else:
          change_direction = True

      result_list.append(mat[x][y])

      # If we change direction, then we need to:
      # - change default vector direction
      # - swap the order of alternative moves: clockwise/counterwise
      if change_direction:
        vectors[0][0] *= -1
        vectors[0][1] *= -1
        vectors[1], vectors[2] = vectors[2], vectors[1]
        change_direction = False

    # Qppending last element. Using "-1" index for shorteness.
    # But it the same as: mat[nrows - 1][ncols - 1].
    result_list.append(mat[-1][-1])

    return result_list

f = Solution()

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')

mat = [[2,5,8],[4,0,-1]]
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')

mat = [[2,5],[4,0], [8,5], [4,3]]
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')

mat = []
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')

mat = [[]]
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')

mat = [[1],[2], [3]]
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')

mat = [[1, 2, 3]]
print(f'Input array: {mat}')
print(f'Answer: {f.diagonal_traverse(mat)}')