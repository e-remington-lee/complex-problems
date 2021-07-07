'''
https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
'''
class SumOfTwoBinary(object):
    def answer1(self, a, b):
        x, y = abs(a), abs(b)
        if x<y:
            x,y = y, x
            a,b = b, a
        
        # sign = 1 if a>0 else -1 
        if a>0:
            sign=1
        else:
            sign=-1   
        if a*b>=0:
            while y:
                answer=x^y
                borrow = (x&y)<<1
                x,y = answer, borrow
        else:
            while y:
                answer = x^y
                carry = ((~x)&y)<<1
                x, y = answer, carry
        return x*sign
print(-6&2)
print(6&2)
x = SumOfTwoBinary()
print(x.answer1(5, -15))
# print(10|7)
# print(10&7)
# print(2|3)
# print(3&2)
# print()
# print(bin(1))
# print(bin(2))
# print(bin(3))
# print(bin(4))
# print(bin(5))
# print(bin(6))
# print(bin(7))
# print(bin(8))
# print(bin(9))
# print(bin(10))
# print(bin(11))
# print(bin(12))
# print(bin(13))
# print(bin(14))
# print(bin(15))


