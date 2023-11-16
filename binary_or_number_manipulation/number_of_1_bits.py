class Solution:
    def hammingWeight(self, n):
        bits = 0
        temp = 1
        for _ in range(32):
            if ((n & temp) != 0):
                bits += 1
            temp = temp << 1
        return bits

    # O(32) space/time
    def pythonic(self, n):
        return bin(n).count("1")
    
    def bit_manipulation2(self, n):
        bits = 0
        '''
        110011 &= 110010 = 110010 add 1
        110010 &= 110001 = 110000 adds 1
        110000 &= 101111 = 100000 adds 1
        100000 &= 011111 = 000000 adds 1, result is 4, crazy this works
        '''
        while n > 0:
            bits += 1
            n &= (n -1)
        return bits

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)
x, y = 12, 8
print(bin(x), bin(x - 1))
print(bin(x & y))