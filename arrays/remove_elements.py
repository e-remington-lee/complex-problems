class Solution:
    def actually_remove(self, nums, val):
        left = 0
        while left <= len(nums) - 1:
            if nums[left] == val:
                nums[left] = nums[len(nums) - 1]
                nums.pop()
            else:
                left += 1
        return left

    def move_to_back(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)