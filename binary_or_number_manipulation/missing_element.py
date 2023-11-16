class Solution:
    def missingNumber(self, nums):
        # Gauss' formula, sum(0, n) inclusive of n 
        total = (len(nums) * (len(nums) + 1)) // 2
        actual = sum(nums)
        return total - actual

    def good_binary(self, nums):
        ans = len(nums)
        for i in range(len(nums)):
            y = i ^ nums[i]
            ans ^= y
        return ans

    #takes up N space
    def bad_binary(self, nums):
        nums.append(0)
        ans = 0
        for i in range(len(nums)):
            y = i ^ nums[i]
            ans ^= y
        return ans

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)