class Solution:
    def binary_search(self, nums, left, right, target):
        if left<right: # right>=left
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
        while left<right: # right>=left
            mid=(right+left)//2
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                return mid
        return left
x=Solution()
nums=[0,1,2,2,3,4,6,7]
print(x.binary_search_iterative(nums, 5))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)