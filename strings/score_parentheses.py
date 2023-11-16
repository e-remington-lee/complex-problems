class Solution:
    def brute(self, s: str) -> int:
        return self.helper(0, len(s), s)
    
    def helper(self, start, stop, s):
        ans = bal = 0
        for i in range(start, stop):
            bal += 1 if s[i] == "(" else -1
            if bal == 0:
                if i - start == 1:
                    ans += 1
                else:
                    ans += 2 * self.helper(start + 1, i, s)
                start = i + 1
        return ans

    def whatIwouldGet(self, s: str) -> int:
        stack = [0]
        
        for x in s:
            if x == "(":
                stack.append(0)
            else:
                value = stack.pop()
                stack[-1] += max(2 * value, 1)
        
        return stack[-1]

    def optimal(self, s: str) -> int:
        ans = bal = 0
        
        for i, x in enumerate(s):
            if x == "(":
                bal += 1
            else:
                bal -= 1
                if s[i-1] == "(":
                    ans += 1 << bal
        return ans

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
