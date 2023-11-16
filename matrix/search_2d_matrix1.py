class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        if len(matrix) == 0:
            return False
        y = len(matrix)
        x = len(matrix[0])
        left, right = 0, y * x - 1
        
        while right >= left:
            mid = (right + left) // 2
            div, mod = divmod(mid, x)
            element = matrix[div][mod]
            if element == target:
                return True
            elif target < element:
                right = mid - 1
            else:
                left = mid + 1
        return False

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)

