from typing import List

class Solution:
  def diagonal_traverse(self, mat: List[List[int]]) -> List[int]:

    # Initial position.
    x = 0
    y = 0

    # Delta by X (rows) and Y (columns).
    xd = -1
    yd = 1
    direction = 0

    # Rows, columns.
    nrows = len(mat)
    ncols = len(mat[0])

    # First value will be 0, 0.
    result_list = [mat[x][y]] 

    for _ in range(nrows * ncols - 2):
        xnew = x + xd
        ynew = y + yd

        if xnew >= 0 and xnew < nrows:
          x = xnew
        else:
          direction -= 1

        if ynew >= 0 and ynew < ncols:
          y = ynew
        else:
          direction -= 1

        # If we can't move by both x and y, moving cursor by coordinate that had 
        # negative delta before. In each moment exactly one directive has 
        # negative delta.
        if direction == -2:
          if xd == -1:
            x += 1
          else:
            y += 1

        # If at least for one directive we reached the boundary, we're changing 
        # direction.
        if direction < 0:
          xd *= -1
          yd *= -1
          direction = 0

        result_list.append(mat[x][y])
        print(f'[{x}][{y}]: {mat[x][y]}')

    result_list.append(mat[nrows-1][ncols-1])

    return result_list

f = Solution()

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(f'Input array: {mat}')
print(f'Answer: [{f.diagonal_traverse(mat)}]')