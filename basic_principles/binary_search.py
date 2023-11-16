class Solution:
    def binary_search(self, nums, left, right, target):
        if left<=right: 
            mid=(right+left)//2
            if target>nums[mid]:
                return self.bs(nums, mid+1, right, target)
            elif target<nums[mid]:
                return self.bs(nums, left, mid-1, target)
            else:
                return mid
        return left

    def binary_search_iterative(self, nums, target):
        left=0
        right=len(nums)-1
        # returns the first value greater than it, with [2,5,8,12,19] target 9, it returns 12. This means it can return an index
        # outside of the range of numbers, returning right will return the first num less than it, can return -1
        while left<=right: 
            mid=(right+left)//2
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                # return True
                return mid
        return left
x=Solution()
nums=[2,5,8,12,19]
print(x.binary_search_iterative(nums, 20))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)