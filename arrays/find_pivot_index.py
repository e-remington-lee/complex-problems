class Solution:
    def pivotIndex(self, nums):
        if len(nums) == 0:
            return -1
        
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == (total - left - nums[i]):
                return i
            else:
                left += nums[i]
        return -1

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)