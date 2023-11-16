class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.new_n(n)
        
        return n == 1
    
    def isHappy_floyds_cycle(self, n: int) -> bool:
        slow = n
        fast = self.new_n(n)
        while slow != 1 and slow != fast:
            slow = self.new_n(slow)
            fast = self.new_n(self.new_n(fast))
        return slow == 1
    
    def new_n(self, n):
        new = 0
        while n > 0:
            div, mod = divmod(n, 10)
            new += mod ** 2
            n = div
        return new
    
    def new_n(self, n):
        new = 0
        while n > 0:
            div, mod = divmod(n, 10)
            new += mod ** 2
            n = div
        return new


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)