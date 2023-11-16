class Solution:
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        end = nums[-1]
        right = len(nums) - 1
        left = 0
        
        while right >= left:
            mid = (right + left) // 2
            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # elif nums[mid] >= nums[0]:
            #     left = mid + 1
            # else:
            #     right = mid - 1
            elif nums[mid] <= end:
                right = mid - 1
            else:
                left = mid + 1

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)