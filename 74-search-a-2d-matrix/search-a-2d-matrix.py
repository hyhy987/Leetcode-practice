class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        top = 0
        bottom = rows - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        if top > bottom:
            return False
        row = top + (bottom - top) // 2
        begin = 0
        end = len(matrix[0])
        while begin < end:
            mid = begin + (end - begin)//2
            if target <= matrix[row][mid]:
                end = mid
            else:
                begin = mid + 1
        if matrix[row][begin] == target:
            return True
        return False
        