class Solution:
    def solveNQueens(self, n):
        self.diagonals, self.a_diagonals, self.columns = set(), set(), set()
        self.response = []
        self.empty_board = [["." for _ in range(n)] for _ in range(n)]
        self.calculate_collisions(0, n)
        return self.response
    
    def append_board(self):
        answer = []
        for row in self.empty_board:
            answer.append("".join(row))
        self.response.append(answer)
        
    
    def calculate_collisions(self, row, n):
        if row == n:
            self.append_board()
            return
        else:

            for i in range(n):
                diagonal = row - i
                a_diagonal = row + i
                if i in self.columns or diagonal in self.diagonals or a_diagonal in self.a_diagonals:
                    continue
                
                
                self.diagonals.add(diagonal)
                self.a_diagonals.add(a_diagonal)
                self.columns.add(i)
                self.empty_board[row][i] = "Q"
                
                self.calculate_collisions(row + 1, n)
                
                self.diagonals.remove(diagonal)
                self.a_diagonals.remove(a_diagonal)
                self.columns.remove(i)
                self.empty_board[row][i] = "."


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)