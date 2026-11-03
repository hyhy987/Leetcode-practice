from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time = 0
        q = deque() 
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            q.append((nr, nc))
        
            time += 1
        
        if fresh != 0:
            return -1
        else:
            return time 




            
