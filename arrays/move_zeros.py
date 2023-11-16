class Solution(object):
    def answer(self, nums):
        start = 0
        for i, x in enumerate(nums):
            if x != 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
        return nums

    '''
    This is the proposed solution, it makes 1.5 passes through the array which I do not like. The solution above does it all in 1 go
    '''
    def answer2(self, nums):
        start=0
        for i, x in enumerate(nums):
            if x!=0:
                nums[start] = nums[i]
                start += 1
                
        for j in range(start, len(nums)):
            nums[j]=0
        

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
nums = [2, 0, 1,0, 3, 4, 0, 0]
Solution().answer(nums)
print(nums)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)