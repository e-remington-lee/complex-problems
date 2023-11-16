from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        response = current = nums[0]
        
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            response = max(current, response)
        return response

    def answer2(self, nums):
        m=c=nums[0]
        for x in nums[1:]:
            #c is negative and x is positive, then x+c is always less than x, so we set c to x or x+c 
            c=max(x, c+x)
            # this keeps a moving tracker of the larest subarray, when we get a value less than 0, it resets the subarray
            m=max(m, c)
        return m

    #think merge sort
    def merge_sort_esque(self, nums, left, right):
        if left<right: # or right>=left        
            mid = (left+right)//2
            curr=bl=br=0
            for i in range(mid+1, right+1):
                curr+=nums[i]
                br=max(br, curr)

            curr=0
            for i in range(mid-1, left-1, -1):
                curr+=nums[i]
                bl=max(bl, curr)

            bc = nums[mid]+bl+br

            lh = self.helper(nums, left, mid-1)
            rh =self.helper(nums, mid+1, right)
            return max(bc, lh, rh)
        else:
            return -float('inf')

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)