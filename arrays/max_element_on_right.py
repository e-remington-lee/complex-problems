'''
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/
'''
class Solution:
    def replaceElements(self, arr):
        _max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], _max = _max, max(_max, arr[i])
        return arr

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)