class Solution:
    def findNumbers(self, nums):
        response = 0
        for x in nums:
            count = 0
            while x > 0:
                x //= 10
                count += 1
            if count % 2 == 0:
                response += 1
            
        return response


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)