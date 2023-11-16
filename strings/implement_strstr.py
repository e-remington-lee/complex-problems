class Solution:
    '''
    time: O(haystack * needle), string slicing takes N time where N is needle, and iterate through haystack
    space: O(needle), we make a string slice of needle each iteration
    '''
    def brute(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        
        n = len(needle)
        h = len(haystack)        
        kmp_arr = [0]*n        
        needle_pointer = hay_pointer = 0        
        self.make_kmp_helper(kmp_arr, needle)
        
        while hay_pointer < h:
            if haystack[hay_pointer] == needle[needle_pointer]:
                needle_pointer += 1
                hay_pointer += 1
            
            if needle_pointer == n:
                return hay_pointer - needle_pointer
            
            # we increement np and hp on success, checking to make sure we do not double dip
            if hay_pointer < h and haystack[hay_pointer] != needle[needle_pointer]: 
                if needle_pointer != 0:
                    needle_pointer = kmp_arr[needle_pointer - 1]
                else: #np is 0, start over
                    hay_pointer += 1
        return -1
    
    def make_kmp_helper(self, arr, needle):
        n = len(needle)
        start, i = 0, 1
        
        while i < n:
            if needle[start] == needle[i]:
                start += 1
                arr[i] = start
                i += 1
            else:
                if start != 0:
                    start = arr[start - 1]
                else:
                    arr[i] = start
                    i += 1

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)