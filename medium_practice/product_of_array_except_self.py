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
        
        

    def brute(self, nums):
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