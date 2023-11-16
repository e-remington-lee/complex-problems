# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        
        m = len(needle)
        n = len(haystack)
        
        lps = [0] * m
        
        j = i = 0
        
        self.make_lps(needle, lps)
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
                # j = lps[j - 1]
            
            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
        
    def make_lps(self, needle, lps):
        start = 0
        m = len(needle)
        i = 1
        
        while i < m:
            if needle[i] == needle[start]:
                start += 1
                lps[i] = start
                i += 1
            else:
                if start != 0:
                    start = lps[start - 1]
                else:
                    lps[i] = 0
                    i += 1

  
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
Solution().strStr(pat, txt)