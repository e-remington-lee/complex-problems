class Solution:
    def brute(self, nums):
        return sorted([x * x for x in nums])

    def sortedSquares(self, nums):
        response = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[right]) >= abs(nums[left]):
                current = nums[right]
                right -= 1
            else:
                current = nums[left]
                left += 1
            response[i] = current * current
        return response

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)