'''
https://leetcode.com/problems/contains-duplicate/

Time: O n,
Space, O n
'''
class ContainsDuplicates(object):
    def answer(self, arr):
        before=len(arr)
        after=len(set(arr))
        if after!=before:
            return True
        return False

    def answer2(self, nums):
        seen={}
        for x in nums:
            if x in seen:
                return True
            seen[x]="0"
        return False


arr=[1,2,3,1]
x=ContainsDuplicates()
print(x.answer2(arr))

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)