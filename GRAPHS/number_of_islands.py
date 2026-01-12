# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

from typing import List
def islands(grid: List[List[int]]):
    rows = len(grid)
    cols = len(grid[0])
    islands = 0 

    def dfs(i, j):
        if (grid[i][j]==0 or i < 0 or j < 0 or i >= rows or j >= cols):
            return 
        grid[i][j]=0
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i-1, j)
        dfs(i+1, j)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                islands+=1
                dfs(i,j)
    return islands