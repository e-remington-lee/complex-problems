from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = defaultdict(int)
        # for x, y in zip(s, t):
            # map[x] += 1
            # map[y] -= 1
            
        for i in range(len(s)):
            map[s[i]] += 1
            map[t[i]] -= 1
        
        for key, value in map.items():
            if value != 0:
                return False
            
        return True

    def array_solution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
            
        for value in counter:
            if value != 0:
                return False
        return True

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)