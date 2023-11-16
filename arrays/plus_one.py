class Solution:
    def custom(self, digits):
        index = len(digits) - 1
        div, mod = divmod(digits[index] + 1, 10)
        digits[index] = mod
        index -= 1
        
        while div > 0 and index >=0:
            div, mod = divmod(digits[index] + div, 10)
            digits[index] = mod
            index -= 1
        
        if div > 0:
            digits.insert(0, 1)
        
        return digits

    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n):
            current = n - 1 - i
            if digits[current] == 9:
                digits[current] = 0
            else:
                digits[current] += 1
                return digits
        return [1] + digits

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)