class Solution:
    '''
    if we are not guaranteed a majority, we would have to do a second loop to check and make sure that the majority is greater than half
    '''
    def majorityElement(self, nums):
        half = len(nums) // 2
        count = 1
        majority_element = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == majority_element:
                count += 1
            else:
                count -= 1
            if count > half:
                return majority_element
            
            if count == 0:
                majority_element = nums[i]
                count = 1
                
        return majority_element

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
