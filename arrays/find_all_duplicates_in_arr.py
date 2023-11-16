class Solution:
    def optimal(self, nums):
        response = []
        for i, num in enumerate(nums):
            anum = abs(num) - 1
            if nums[anum] > 0:
                nums[anum] *= -1
            else:
                response.append(abs(num))
        return response
    
    def got_first_try(self, nums):
        for i, num in enumerate(nums):
            anum = abs(num) - 1
            if nums[anum] > 0:
                nums[anum] *= -1
            
        for i, num in enumerate(nums):
            anum = abs(num) - 1
            nums[anum] *= -1
        
        return [i for i in range(1, len(nums) + 1) if nums[i - 1] < 0]

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
