class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        start = 0
        for i, x in enumerate(s):
            if x in seen and start <= seen[x]:
                start = seen[x] + 1
            else:
                cur = i - start + 1
                ans = max(ans, cur)
            seen[x] = i
        return ans

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard) 