class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        left, right = 0, len(arr) - 1
        while left <= right:
            if left == right and arr[left] == 0:
                right -= 1
                arr[-1] = 0
                break
            elif arr[left] == 0:
                zeros += 1
                right -= 1
            left += 1
        
        
        for i in range(right, -1, -1):
            if arr[i] == 0:
                arr[i + zeros] = 0
                zeros -= 1
                arr[i + zeros] = 0
            else:
                arr[i + zeros] = arr[i]

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)