from collections import deque
class Solution:
    def factory_methods(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split()])

    def reverseWords(self, s: str) -> str:
        self.response = []
        self.s = s
        
        start = stop = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(start, i)
                start = i + 1
        self.reverse(start, len(s))
        
        return " ".join(self.response)
        
    def reverse(self, start, end):
        word = deque()
        for i in self.s[start:end]:
            word.appendleft(i)
            
        self.response.append("".join(word))


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
