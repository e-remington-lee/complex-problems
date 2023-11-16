class Solution:
    def fav(self, s):
        _map={"{": "}", "(": ")", "[": "]"}
        stack=[]
        for i in s:
            if s in _map:
                stack.append(s)
            elif not stack or _map[stack.pop()]!=i:
                return False
        return not stack

    def reverse(self, s: str) -> bool:
        _map={"}": "{", ")": "(", "]": "["}
        stack=[]
        for i in s:
            if i in _map:
                if not stack:
                    return False
                if stack and stack.pop()!=_map[i]:
                    return False
            else:
                stack.append(i)
        return not stack

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)