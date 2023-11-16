# https://leetcode.com/problems/first-unique-character-in-a-string/solution/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m={}
        for i, x in enumerate(s):
            if x not in m:
                m[x]=False
            else:
                m[x]=True
        
        for i,x in enumerate(s):
            if not m[x]:
                return i
        return -1


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

'''
can't do it in 1 pass bc we need to see the whole string to determine if it has not repeated

need a data structure to reference what chars we have seen, hashmap works
'''