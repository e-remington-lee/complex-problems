# 2 = 00010
# 5 = 00101
# XOR

'''
2 is not a member of 5, we cannot break up 5 into, meaning we cannot do bitwise & to a 2 and get 5. In this case the response is we add them

2^3, 2 is a member of 3 bc to get 011, we can add 010 and 001,so 2^3 returns 1

2^6, 6= 0110, 4=0100, so 2^6 gives 4. 
'''
# print(10<<1)
# print(~1)
# print(0b111)
# print(2^3)
# 0011
# 0111
x, y = 3, 7
x = x ^ y
# 0011 ^ 0111: x = 0100 = 4
print(x)

# 0100 ^ 0111 y = 0011 = 3
y = x ^ y 
print(y)

# 0100 ^ 0011 = 0111 = 7
x = x ^ y 

def strToBinary(s):
    bin_conv = []
 
    for c in s:
         
        # convert each char to
        # ASCII value
        ascii_val = ord(c)
         
        # Convert ASCII value to binary
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])
         
    return (' '.join(bin_conv))
 
# Driver Code
if __name__ == '__main__':
    s = '0100'
 
print (strToBinary(s))