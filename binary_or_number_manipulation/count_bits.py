class Solution:
    def countBits(self, n):
        response = []
        for i in range(n + 1):
            num = i
            bits = 0
            while num > 0:
                bits += 1
                num &= (num - 1) 
            response.append(bits)
        return response
    
    # bit wise problems fucking suck, idk how you can just figure this out wtf
    def dp_lsb(self, n):
        response = [0] * (n + 1)
        for i in range(1, n + 1):
            response[i] = response[i >> 1] + (i & 1)
        return response


    # lsb/msb is least/most significant bit. msb is usually whether or not it is negative or not
    def dp_last_set_bit(self, n):
        response = [0] * (n + 1)
        for i in range(1, n + 1):
            response[i] = response[i & (i - 1)] + 1
        return response


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)