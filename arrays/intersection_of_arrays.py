class Solution:
    # interesction means common elements between the 2
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]
    

    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        return set1.intersection(set2)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)