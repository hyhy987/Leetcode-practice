class Solution(object):
    def isValidSudoku(self, board):
        height = len(board)
        width = len(board[0])

        for i in range(height):
            new = set()
            for j in range(width):
                if board[i][j] == ".":
                    continue
                if board[i][j] in new:
                    return False
                else:
                    new.add(board[i][j])

        for j in range(width):
            new = set()
            for i in range(height):
                if board[i][j] == ".":
                    continue
                if board[i][j] in new:
                    return False
                else:
                    new.add(board[i][j])

        for i in range(0, height, 3):
            for j in range(0, width, 3):
                new = set()
                for n in range(3):
                    for m in range(3):
                        if board[i+n][j+m] == ".":
                            continue
                        if board[i+n][j+m] in new:
                            return False
                        else:
                            new.add(board[i+n][j+m])

        return True