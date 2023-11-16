# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.



class Solution(object):
    def brute(self, arr, num):
        _sum=sum(arr)
        length = len(arr)
        if _sum<num:
            return 0
        if _sum==num:
            return length

        best=length
        for i in range(len(arr)):
            for j in range(len(arr)):
                if sum(arr[i:j+1])>=num and len(arr[i:j+1])<best:
                    best=len(arr[i:j+1])
        return best


    def minSubArrayLen(self, target, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                return 0
        
        left, right = 0, 1
        response = float("inf")
        current = nums[0]
        while left < len(nums):
            if current >= target:
                response = min(response, right - left)
                current -= nums[left]
                left += 1
            elif current < target and right < len(nums):
                current += nums[right]
                right += 1
            else: #it is less than, but right is at the end
                left += 1
                
        
        return response if response != float("inf") else 0

    def optimal(self, target, nums):
        _sum = sum(nums)
        if _sum < target:
            return 0
        if _sum == target:
            return len(nums)
        l, r = 0, -1
    
        length = len(nums)
        _sum = 0
        while l < len(nums):
            if _sum < target and r + 1 < len(nums):
                r += 1
                _sum += nums[r]
            else:
                _sum -= nums [l]
                l += 1
            if _sum >= target:
                length = min(r - l + 1, length)
        return length


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
