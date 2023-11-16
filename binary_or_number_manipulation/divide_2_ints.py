class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_int = 2**31 -1
        min_int = -2**31
        half = -1073741824 # can't use division
        
        if dividend == min_int and divisor == -1:
            return max_int
        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
            
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
            
        if dividend > divisor:
            return 0
        
        quotient = 0
        power = -1
        value = divisor 
        
        # negative values
        while value >= half and value + value >= dividend:
            value += value
            power += power
            
        while divisor >= dividend:
            if value >= dividend:
                quotient += power
                dividend -= value   
            power = (power >> 1)
            value = (value >> 1)
            
        return quotient if negatives is 1 else -quotient


    def memo(self, dividend: int, divisor: int) -> int:
        powers = []
        values = []
        max_int = 2**31 -1
        min_int = -2**31
        half = -1073741824 # can't use division
        
        if dividend == min_int and divisor == -1:
            return max_int
        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
                    
        quotient = 0
        power = -1
        value = divisor 
        
        while divisor >= dividend:
            values.append(value)
            powers.append(power)
            if half > value:
                break
            
            value += value
            power += power
        
        for i in range(len(values)-1, -1, -1):
            if values[i] >= dividend:
                quotient += powers[i]
                dividend -= values[i]          
            
        return quotient if negatives is 1 else -quotient

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)