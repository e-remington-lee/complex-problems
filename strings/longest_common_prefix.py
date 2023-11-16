class Solution:
    def vertical_search(self, strs):
        prefix = []
        first = strs[0]
        for i in range(len(first)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or first[i] != strs[j][i]:
                    return "".join(prefix)
            prefix.append(first[i])
        return "".join(prefix)
    
    def horizontal_search(self, strs):
        prefix = strs[0]
        for j in range(1, len(strs)):
            while strs[j].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

'''
horizontal search, abc is the second word, we use abcde as the prefix. If all the words are the same, it returns itself!
but most of the time it will slowly pop off indexes.

str.find(str) takes N + M time in optimized python 3, or maybe N*M, so you would think the horizontal one would be much worse, but the fact we update
the prefix on each go makes it very optimal in practice
'''
print("abc".find("abcde"))
print("abc".find("abcd"))
print("abc".find("abc"))

print("aback".find("abc"))
print("aback".find("ab"))

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)