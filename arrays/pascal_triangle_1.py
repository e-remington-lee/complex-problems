class Solution:
    def generate(self, numRows: int):
        response=[[1]]
        for i in range(1, numRows):
            li=[1]*(i+1)
            for j in range(i+1):
                if j==0 or j==i:
                    li[j]=1
                else:
                    li[j]=response[i-1][j]+response[i-1][j-1]
            response.append(li)    
        return response

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)