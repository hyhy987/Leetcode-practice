class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])

        startRow, endRow = 0, numRows - 1
        # Find row, target row is the endRow
        while startRow < endRow: 
            midRow = startRow + (endRow - startRow) // 2 
            if matrix[midRow][0]<= target <= matrix[midRow][numCols-1]:
                endRow = midRow
                break
            elif target < matrix[midRow][0]:
                endRow = midRow
            else:
                startRow = midRow + 1

        # Find col 
        startCol, endCol = 0, numCols - 1

        while startCol < endCol:
            midCol = startCol + (endCol - startCol) // 2
            if target <= matrix[endRow][midCol]:
                endCol = midCol
            else:
                startCol = midCol + 1

        print(matrix[endRow][endCol])
        
        return matrix[endRow][endCol] == target
