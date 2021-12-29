from typing import List


class Solution:
    def spiral_matrix(self, matrix: List[List[int]]) -> List[int]:
        # Output list.
        result_list = []

        # If list is empty.
        if not matrix:
            return result_list

        # Rows, columns.
        nrows = len(matrix)
        ncols = len(matrix[0])
        nelements = nrows * ncols

        # if array is flat or empty, then there is not need to traverse the matrix
        # by diagonal.
        if nrows < 2 or ncols < 2:
            for row in matrix:
                for element in row:
                    result_list.append(element)
            return result_list

        # Initial position.
        x = 0
        y = 0

        # Initial vector.
        xd = 0
        yd = 1

        # Adding initial point.
        result_list.append(matrix[x][y])

        visited_elements = set()
        visited_elements.add((0, 0))

        for _ in range(nelements - 1):

            # Only 4 possible directions.
            for _ in range(4):
                xnew = x + xd
                ynew = y + yd

                if any([
                    xnew < 0 or xnew == nrows,
                    ynew < 0 or ynew == ncols,
                    (xnew, ynew) in visited_elements
                ]):
                    # Rotating direction vector clockwise (x, y) -> (y, -x).
                    xd, yd = yd, -xd
                else:
                    x = xnew
                    y = ynew
                    break

            visited_elements.add((x, y))
            result_list.append(matrix[x][y])

        return result_list

f = Solution()

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[2, 5, 8], [4, 0, -1]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[2, 5], [4, 0], [8, 5], [4, 3]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = []
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[1], [2], [3]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')

mat = [[1, 2, 3]]
print(f'Input array: {mat}')
print(f'Answer: {f.spiral_matrix(mat)}')
