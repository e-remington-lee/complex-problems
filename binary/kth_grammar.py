# video help https://www.youtube.com/watch?v=QRa9ZVGMWlY
# https://leetcode.com/problems/k-th-symbol-in-grammar/
class Solution:
    def kthGrammar(self, n, k):
        if n==1: return 0
        parent = self.kthGrammar(n-1, k//2+k%2)
        odd=(k%2==1)
        if parent==1:
            return 1 if odd else 0
        else:
            return 0 if odd else 1

    def brute(self, n, k):
        prev='0'
        c=[]
        for i in range(1, n):
            for s in prev:
                if s=='0':
                    c.extend(['0', '1'])
                elif s=='1':
                    c.extend(['1', '0'])
            prev=''.join(c)
            c=[]
        return prev[k-1]

x = Solution()
# print(x.answer(3,3))

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)