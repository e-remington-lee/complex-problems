# https://leetcode.com/problems/maximum-product-subarray/solution/
class Solution:
    def maxProduct(self, nums):
        _max = temp_max = _min = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            temp_max, _min = max(x, x*_min, temp_max*x) ,min(x, _min*x, temp_max*x)
            _max = max(_max, temp_max)
        return _max


    '''
    O(2n), linear time, constant space
    '''
    def two_pass(self, nums):
        m=nums[0]
        c=1
        for x in nums:
            c*=x
            m=max(c, m)
            if c==0:
                c=1
        c=1
        for x in reversed(nums):
            c*=x
            m=max(c, m)
            if c==0:
                c=1
        return m


    def brute(self, nums):
        m=nums[0]
        for i in range(len(nums)):
            c=1
            n=False
            for j in range(i, len(nums)):
                c*=nums[j]
                if c<0:
                    n=True
                else:
                    n=False
                if not n:
                    m=max(c, m)
        return m

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)