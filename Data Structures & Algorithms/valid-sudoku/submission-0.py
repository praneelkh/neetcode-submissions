class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Check
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[i][j]
                if num in seen:
                    return False
                elif num != ".":
                    seen.add(num)

        # Col Check
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[j][i]
                if num in seen:
                    return False
                elif num != ".":
                    seen.add(num)

        # Box Check
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3, 3), (3,6), 
                  (6, 0), (6,3), (6,6)]
        
        for i, j in starts:
            seen = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    num = board[row][col]
                    if num in seen:
                        return False
                    elif num != ".":
                        seen.add(num)
        return True

        