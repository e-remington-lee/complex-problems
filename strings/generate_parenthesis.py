import itertools
class Solution:
    def brute(self, n: int):
        s="()"
        temp=set()
        # itertools.product returns the cartesian product of the javaPractice, or the iteratble with length of repeat=n with contents being combinations of that
        # which equal the n length. s^n
        for p in itertools.product(s, repeat=n*2):
            temp.add("".join(p))
        output=[]
        for x in temp:
            if self.validate(x):
                output.append(x)
        return output
    
    def validate(self, s):
        _map={"(":")"}
        stack=[]
        for i in s:
            if i in _map:
                stack.append(i)
            elif not stack or _map[stack.pop()]!=i:
                return False
        return not stack

    def generateParenthesis(self, n):
        self.answer = []
        self.backtrack([], 0, 0, n)
        return self.answer
        
        
    def backtrack(self, current, openings, closings, n):
        if len(current) == 2*n:
            self.answer.append("".join(current[:]))
        else:
            if openings < n:
                current.append("(")
                self.backtrack(current, openings+1, closings, n)
                current.pop()
            if closings < openings:
                current.append(")")
                self.backtrack(current, openings, closings+1, n)
                current.pop()

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
