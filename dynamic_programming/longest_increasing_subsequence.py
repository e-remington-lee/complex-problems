'''
https://leetcode.com/problems/longest-increasing-subsequence/discuss/?currentPage=1&orderBy=most_votes&query=

'''
class LongestIncreasingSubsequence(object):
    def my_answer(self, nums):
        hm={}
        _max=1
        for x in nums:
            temp_max=1
            for key in hm.keys():
                if key<x:
                    temp_max = max(temp_max, hm[key]+1)
                elif key==x:
                    temp_max=max(temp_max, hm[key])
            hm[x]=temp_max
            _max=max(_max, temp_max)
        return _max

    '''
    Once you realize the first iteration does nothing, you can optimize to range(1, len(nums)), but don't worry about that at first,
    bc you are more likely to fuck up, the first implementation does not have to be 100% right, just needs to work 
    
    time n^2, space n
    '''
    def answer1(self, nums):
        dp = [1]*len(nums)
        m=1
        for i in range(len(nums)):
            for j in range(len(nums[:i])):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
                    m=max(m, dp[i])
        return m

    def answer2(self, nums):
        response=[nums[0]]
        for num in nums[1:]:
            if num>response[-1]:
                response.append(num)
            else:
                i=0
                while num>response[i]:
                    i+=1
                response[i]=num
        return len(response)

    '''
    time: O(log(n)*n), we search through the entire num list and do a binary search each time
    space: O (n), we can have a list of all the numbers at worst
    '''
    def optimal(self, nums):
        response=[nums[0]]
        for num in nums:
            i = self.binary_search_iterative(response, num)
            if i == len(response):
                response.append(num)
            else:
                response[i]=num
        return len(response)

    '''
    Making it really optimal, runs faster, ect,
    '''
    def optimal2(self, nums):
        sub = [nums[0]]
        for num in nums[1:]:
            # If num is greater than the last element (which is the largest)
            if num>sub[-1]:
                sub.append(num)
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                i = self.binary_search_iterative(sub, num)
                sub[i]=num
        return len(sub)

    def binary_search(self, nums, left, right, target):
        if right>=left:
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
        while right>=left:
            mid=(right+left)//2
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                return mid
        return left


a=[1,3,4,6]
            
from bisect import bisect_left
# print(bisect_left(a, 6))


nums=[0,3,1,6,2,2,7]
x=LongestIncreasingSubsequence()
print(x.answer2(nums))
print(x.binary_search_iterative(a, 5))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)