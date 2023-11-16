class Solution:
    def thirdMax(self, nums):
        max_set = set()
        for x in nums:
            max_set.add(x)
            if len(max_set) > 3:
                max_set.remove(min(max_set))
        
        if len(max_set) < 3:
            return max(max_set)
        else:
            return min(max_set)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)