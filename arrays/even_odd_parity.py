class Solution:
    def sortArrayByParity(self, nums):
        even, odd = 0, len(nums) - 1
        while even < odd:
            if nums[even] % 2 != 0:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd -= 1
            else:
                even += 1
        return nums


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)