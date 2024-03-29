class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:]
        
        i = j = k = 0
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while i < m:
            nums1[k] = nums1_copy[i]
            k += 1
            i += 1
        
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)