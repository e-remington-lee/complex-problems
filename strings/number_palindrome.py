class Solution:
    def isPalindrome(self, x: int) -> bool:
        # need this check for anything that ends in 0, like 10 or 100
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        response = 0
        final = x
        while final > response:
            response = response * 10 + x % 10
            x //= 10
        
        return final == response
        
    def brute(self, x):
        if x < 0:
            return False
        
        s = str(x)
        return s == s[::-1]
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)