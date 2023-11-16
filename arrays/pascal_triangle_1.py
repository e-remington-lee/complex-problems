class Solution:
    def generate(self, numRows):
        response = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    num = response[i - 1][j] + response[i - 1][j - 1]
                    row.append(num)
            response.append(row)
        return response

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)