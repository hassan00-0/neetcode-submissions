class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val == ".":
                    continue

                row_key = (i, val)
                column_key = (val, j)
                box_key = (i//3, j//3, val)

                if row_key in seen or column_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)
        return True
        
