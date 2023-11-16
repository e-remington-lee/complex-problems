class Solution:
    def findDiagonalOrder(self, mat):
        if not mat:
            return []
        
        response = []
        end_row = len(mat) - 1
        end_col = len(mat[0]) - 1
        
        up = True
        row, col = 0, 0
        while True:
            response.append(mat[row][col])
            if row == end_row and col == end_col:
                return response
            if up:
                if row - 1 < 0 or col + 1 > end_col:
                    if col + 1 <= end_col:
                        col += 1
                    else:
                        row += 1
                    up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row + 1 > end_row or col - 1 < 0:
                    if row + 1 <= end_row:
                        row += 1
                    else:
                        col += 1
                    up = True
                else:
                    row += 1
                    col -= 1


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)