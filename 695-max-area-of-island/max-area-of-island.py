from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])

        ones = set()
        maxArea = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ones.add((i, j))

        visited = set() 

        for elem in ones:

            if elem in visited:
                continue
            q.append(elem)
            currCount = 1

            while q:
                curr = q.popleft()
                r, c = curr
                visited.add(curr)

                for delta in directions:
                    dr, dc = delta
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) not in visited and grid[nr][nc] == 1:
                            currCount += 1
                            q.append((nr, nc))
                            visited.add((nr, nc))
            maxArea = max(maxArea, currCount)
    
        return maxArea 


        