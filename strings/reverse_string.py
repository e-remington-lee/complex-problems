class Solution:
    def recursive(self, s):
        self.helper(0, len(s) -1 , s)
        
    def helper(self, left, right, s):
        if right > left:
            s[left], s[right] = s[right], s[left]
            self.helper(left + 1, right - 1, s)

    def iterative(self, s):
        left, right = 0, len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
    
    def slicing(self, s):
        '''
        start, stop, step. you could do s[len(s):-1]
        '''
        return s[::-1]

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

a = [1,2,3,4,5]
print(a[len(a)-1::-1])