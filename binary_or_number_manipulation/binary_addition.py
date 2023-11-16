from collections import deque
class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        out = deque()
        carry = 0
        for i in range(n - 1, -1, -1):
            x = int(a[i])
            y = int(b[i])
            current = x + y + carry
            
            if current % 2 == 1:
                out.appendleft("1")
            else:
                out.appendleft("0")
            carry = current // 2
        if carry == 1:
            out.appendleft("1")
        return "".join(out)

    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b,2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    def brute(self, a, b):
        return bin((int(a, 2) + int(b, 2)))[2:]


    def my_solution(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        carry = 0
        ans = []
        while i >= 0 and j >= 0:
            x = int(a[i])
            y = int(b[j])
            current = x + y + carry
            if current is 3:
                ans.insert(0, "1")
                carry = 1
            elif current is 2:
                ans.insert(0, "0")
                carry = 1
            elif current is 1:
                ans.insert(0, "1")
                carry = 0
            else:
                ans.insert(0, "0")
                carry = 0
            i -= 1
            j -= 1
        
        while i >= 0:
            x = int(a[i])
            current = x + carry
            if current is 2:
                ans.insert(0, "0")
                carry = 1
            else:
                ans.insert(0, str(current))
                carry = 0
            i -= 1
            
        while j >= 0:
            x = int(b[j])
            current = x + carry
            if current is 2:
                ans.insert(0, "0")
                carry = 1
            else:
                ans.insert(0, str(current))
                carry = 0
            j -= 1
        
        if carry is not 0:
            ans.insert(0, str(carry))
        
        return "".join(ans)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
x = "0100"
print(int(x, 2))

y = "{0:b}".format(7)
print(y)
print(type(y))
