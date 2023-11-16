class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            
            if nums[index] > 0:
                nums[index] *= -1
            
        response = []
        for i in range(len(nums)):
            if nums[i] > 0:
                response.append(i + 1)
        return response


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)