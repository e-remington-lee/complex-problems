# https://leetcode.com/problems/powx-n/solution/
class Solution:
    # THINK if n is negative, then we are just doing 1/x instead of x
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        
        if n%2==1:
            A = self.myPow(x, n // 2)
            return A * A * x
        else:
            A = self.myPow(x, n // 2)
            return A * A

    def optimal_iterative(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        r=1
        c=x
        # we need the r/c bc we cannot double count the odd increments when we just multiply by c, if we do r*=x, and on even r*=r, then we
        # double count that individual x that was multiplied that should not have been there. pow(2, 10)
        # using this method, yes the c is eventually squared with c*=c, but in the case of 3^10=3^(5*2), so it does work out
        while n:
            if n%2==1:
                n-=1
                r *= c
            c *= c
            n//=2
        return r

    # THINK if n is negative, then we are just doing 1/x instead of x
    def linear_multiply(self, x, n):
        if n<0:
            x=1/x
            n=-n
        r=1
        for i in range(n):
            r*=x
        return r
        
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
