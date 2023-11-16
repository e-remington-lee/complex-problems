class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        cur = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] != cur:
                cur = nums[i]
                nums[count] = nums[i] 
                count += 1
        return count

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)
print(2 ^ 3)
