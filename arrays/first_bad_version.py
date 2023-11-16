class Solution:
    def firstBadVersion(self, n):
        def isBadVersion(n):
            pass
        low = 0
        high = n
        while high >= low:
            mid = (low + high) // 2
            if isBadVersion(mid):
                if mid != 0:
                    if not isBadVersion(mid - 1):
                        return mid
                else:
                    return mid
                high = mid
            else:
                if mid != n:
                    if isBadVersion(mid + 1):
                        return mid + 1
                else:
                    if isBadVersion(mid):
                        return mid
                low = mid


    def optimized_binary_search(self, n):
        def isBadVersion(n):
            pass
        low = 0
        high = n
        while high >= low:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)