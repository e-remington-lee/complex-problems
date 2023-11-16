from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        self.backtracking(nums, set(), [], output)
        return output
    
    def backtracking(self, nums, seen, current, output):
        if len(current)==len(nums):
            output.append(current[:])
        else:
            for x in nums:
                if x not in seen:
                    current.append(x)
                    seen.add(x)
                    self.backtracking(nums, seen, current, output)
                    current.pop()
                    seen.remove(x)

                    
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        output=[]
        permuations = itertools.permutations(nums, len(nums))
        for x in permuations:
            output.append(list(x))
        return output

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)