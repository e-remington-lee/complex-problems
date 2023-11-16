class Solution:
    def findMaxConsecutiveOnes(self, nums):
        if len(nums) == 1 and nums[0] == 1:
            return 1
        prev_ones = 0
        cur_ones = 0
        response = 0
        swapped = False
        for x in nums:
            if x == 0:
                response = max(cur_ones + prev_ones + 1, response)
                prev_ones, cur_ones = cur_ones, 0
                swapped = True
            else:
                cur_ones += 1
        
        if swapped:
            response = max(response, cur_ones + prev_ones + 1)
        else:
            response = max(response, cur_ones)
        return response


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)