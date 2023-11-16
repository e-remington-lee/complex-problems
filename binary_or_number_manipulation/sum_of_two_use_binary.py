'''
https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
'''
class SumOfTwoBinary(object):
    def answer1(self, a, b):
        x, y = abs(a), abs(b)
        if x < y:
            a, b = b, a
            x, y = y, x
        
        sign = 1 if a > 0 else -1
        if a * b > 0:
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        return x * sign

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

def idfk(x, y):
    while y:
        answer = x ^ y
        borrow = ((~x) & y) << 1
        x, y = answer, borrow
    return x

# print(idfk(3, 2))
x, y = 9, 7
while y:
    x, y = x ^ y, ((~x) & y) << 1
print(x)
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


