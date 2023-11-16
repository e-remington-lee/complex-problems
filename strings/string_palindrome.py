class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while right >= left:
            while right > left and not s[right].isalnum():
                right -=1
            while right > left and not s[left].isalnum():
                left += 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True

    def brute(self, s: str) -> bool:
        lower = [x.lower() for x in s if x.isalnum()]
        
        return list(lower) == lower[::-1]

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)