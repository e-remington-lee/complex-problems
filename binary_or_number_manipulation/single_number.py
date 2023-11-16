class Solution:
    def singleNumber(self, nums) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans


    def math(self, nums):
        return 2*sum(set(nums)) - sum(nums)


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard) 