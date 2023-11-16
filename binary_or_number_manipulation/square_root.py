class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while right >= left:
            mid = (left + right) // 2
            mid_val = mid * mid
            if mid_val < x:
                left = mid + 1
            elif mid_val > x:
                right = mid - 1
            else:
                return mid
        return right


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)