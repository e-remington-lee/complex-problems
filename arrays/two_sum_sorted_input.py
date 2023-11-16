class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while right > left:           
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1
        

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)