'''
https://leetcode.com/problems/product-of-array-except-self/

time: O(2n)
space: constant if we do not include the return statement
'''
class ProductArrayExceptSelf(object):
    def answer(self, nums):
        value=1
        response=[]
        for i in range(len(nums)):
            response.append(value)
            value*=nums[i]
        value=1
        for i in range(len(nums)-1, -1, -1):
            response[i]*=value
            value*=nums[i]
        return response
        
    def brute1(self, nums):
        response1=[]
        response2=[]
        r3=[]
        s=1
        for i, x in enumerate(nums):
            s*=x
            response1.append(s)
        s=1
        for i in range(len(nums)-1, -1, -1):
            s*=nums[i]
            response2.insert(0, s)      
        for i in range(len(response1)):
            a=i-1
            b=i+1
            if a<0 or a>len(response1)-1:
                x=1
            else:
                x=response1[a]
            if b<0 or b>len(response1)-1:
                y=1
            else:
                y=response2[b]
            r3.append(y*x)
        return r3


    def brute2(self, nums):
        response=[]
        for i, x in enumerate(nums):
            s=1
            for j, y in enumerate(nums):
                if j==i:
                    continue
                else:
                    s*=y
            response.append(s)
        return response
        
    #doesn't actually work, but good concept, a 0 value makes it fail
    def cool(self, nums):
        response=[]
        value=None
        for i in range(len(nums)):
            for j in range(0, i):
                if value:
                    value*=nums[j]
                else:
                    value=nums[j]
            for k in range(i+1, len(nums)):
                if value:
                    value*=nums[k]
                else:
                    value=nums[k]
            response.append(value)
            value=None
        return response


nums=[1,2,3,4]
x = ProductArrayExceptSelf()
print(x.answer(nums))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)