class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            largest_index = 0
            second_index = 1
        else:
            largest_index = 1
            second_index = 0
        
        for i in range(2, len(nums)):
            if nums[i] > nums[largest_index]:
                largest_index, second_index = i, largest_index
            elif nums[i] > nums[second_index]:
                second_index = i
            
        return largest_index if  nums[largest_index] >= nums[second_index] * 2 else -1

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)