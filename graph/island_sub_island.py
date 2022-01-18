from typing import List


class Solution:
    DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        result = 0
        for row_idx in range(len(grid2)):
            for col_idx in range(len(grid2[0])):
                if (row_idx, col_idx) not in visited and grid2[row_idx][col_idx] == 1:
                    if self._helper(grid1, grid2, row_idx, col_idx, visited) == False:
                        visited.remove((row_idx, col_idx))
                        self._mark_visited(grid2, row_idx, col_idx, visited)
                    elif self._helper(grid1, grid2, row_idx, col_idx, visited) != False:
                        result += 1
        return result

    def _helper(self, grid1, grid2, row_idx, col_idx, visited):
        visited.add((row_idx, col_idx))
        if grid2[row_idx][col_idx] == 1:
            if grid1[row_idx][col_idx] == 1:
                for row_inc, col_inc in Solution.DIRECTION:
                    new_row = row_idx + row_inc
                    new_col = col_idx + col_inc
                    if 0 <= new_row < len(grid2) and 0 <= new_col < len(grid2[0]) and (new_row, new_col) not in visited and grid2[new_row][new_col] == 1:
                        if self._helper(grid1, grid2, new_row, new_col, visited) == False:
                            visited.remove((new_row, new_col))
                            return False
            else:
                self._mark_visited(grid2, row_idx, col_idx, visited)
                return False

    def _mark_visited(self, grid, row_idx, col_idx, visited):
        visited.add((row_idx, col_idx))
        for row_inc, col_inc in Solution.DIRECTION:
            new_row = row_idx + row_inc
            new_col = col_idx + col_inc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited and \
                    grid[new_row][new_col] == 1:
                self._mark_visited(grid, new_row, new_col, visited)


grid1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
grid2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]

grid1a = [[0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
          [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
          [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
          [1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 1, 1, 0, 1, 1, 1, 1]]

grid2a = [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
          [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
          [1, 0, 0, 1, 0, 0, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
          [1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 0]]

s = Solution()
print(s.countSubIslands(grid1a, grid2a))
