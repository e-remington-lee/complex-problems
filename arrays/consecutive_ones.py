'''
I only included this bc the for loop does not work, what if the last 3 items are the max? we never get to check bc of the for loop,
so after the loop we have to check again 1 final time
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        response, current = 0, 0
        for x in nums:
            if x == 1:
                current += 1
            else:
                response = max(response, current)
                current = 0
                
        return max(response, current)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)