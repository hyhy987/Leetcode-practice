class Solution(object):
    def numIslands(self, grid):
        count = 0
        visited = set()

        def dfs(grid, row, col, visited):
            if (row < 0 or row >= len(grid) or 
                col < 0 or col >= len(grid[0]) or 
                grid[row][col] == '0' or 
                (row, col)in visited):

                return 

            visited.add((row, col))

            dfs(grid, row - 1, col, visited) #up
            dfs(grid, row + 1, col, visited) #down
            dfs(grid, row, col - 1, visited) #left
            dfs(grid, row, col + 1, visited) #righted

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs (grid, i, j, visited)
                    count += 1

        return count
