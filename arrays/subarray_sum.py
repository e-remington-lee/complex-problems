'''
https://leetcode.com/discuss/interview-question/1715973/Vmware-or-Phone-or-subarray-sum
Given an array of integers, form three sub arrays s1, s2, s3 such that
sum(s2) <= sum(s1)+sum(s3).
Return the number of such subarrays that can be formed

Eg)
Input
[2,3,5,7]
Output
3
Explanation
subarrays are

s1 = [2], s2 = [3], s3 = [5,7]
s1 = [2,3], s2 = [5], s3 = [7]
s1 = [2], s2 = [3,5], s3 = [7]




closest I could find
https://www.techiedelight.com/3-partition-problem/
'''


class Solution:
    def answer(self, nums):
        if len(nums) < 3:
            return 0
        nums.sort()
        response = 0
        for i in range(len(nums) - 2):
            left_sum = sum(nums[:i + 1])
            right_sum = sum(nums[i + 1:])
            '''
            I started with backtracking, which I think can work
            but I realized that if it is sorted, and I know the left sum <= right sum, then I can just find the combinations of numbers on the right
            and add that to the response, bc that is how many combinations there will be
            2, 3, 5, 7
            2 as left sum, we have 3 5 7, which can be 3, 5 7, or 3 5 , 7. it is 1 less than the length of the numbers. So do that!
            '''
            if left_sum <= right_sum: 
                response += len(nums) - i - 2
        return response


    # def backtracking1(self, nums, index, li1, li2, li3):
    #     if index == len(nums):
    #         return

    #     for i in range(index, len(nums) - 1):
    #         li2 += sum(nums[index: i + 1] )
    #         self.backtracking2(nums, i + 1, li1, li2, li3)
    #         li2 -= sum(nums[index])

    # def backtracking2(self, nums, index, li1, li2, li3):
    #     if index == len(nums) and li1 <= li2 + li3:
    #         self.response += 1
    #         return
    
    #     if index == len(nums):
    #         return

    #     for i in range(index):
    #         li3 += sum(nums[index: i + 1] )
    #         self.backtracking2(nums, i + 1, li1, li2, li3)
    #         li3 -= sum(nums[index])
        




X = Solution()
print(X.answer([8, 2,3,5,7]))
print(X.answer([2,3,5,7]))