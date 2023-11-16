from collections import deque
class Solution:

    def reverse_parts(self, nums, k):
        k = k % len(nums)
        if k != 0: 
            self.reverse(0, len(nums) - 1, nums)
            self.reverse(0, k - 1, nums)
            self.reverse(k, len(nums) - 1, nums)
    
    def reverse(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def brute_with_optimization(self, nums, k):
        true_rotations = k % len(nums)
        final = [0] * len(nums)
        for i in range(len(nums)):
            final[(i + true_rotations) % len(nums)] = nums[i]
        
        nums[:] = final

    def custom_deque(self, nums, k):
        true_rotations = k % len(nums)
        final = deque(nums)
        for _ in range(true_rotations):
            num = final.pop()
            final.appendleft(num)
        
        nums[:] = final

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)