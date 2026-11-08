class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in row[r]:
                    return False
                if board[r][c] in column[c]:
                    return False
                if board[r][c] in square[(c // 3, r // 3)]:
                    return False

                row[r].add(board[r][c])
                column[c].add(board[r][c])
                square[(c // 3, r // 3)].add(board[r][c])

        return True