# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.



class Solution(object):
    def brute(self, arr, num):
        _sum=sum(arr)
        length = len(arr)
        if _sum<num:
            return 0
        if _sum==num:
            return length

        best=length
        for i in range(len(arr)):
            for j in range(len(arr)):
                # print(sum(arr[i:j]))
                # print(len(arr[i:j]))
                if sum(arr[i:j+1])>=num and len(arr[i:j+1])<best:
                    best=len(arr[i:j+1])
        return best


    # slightly better than the double for-loop using ranges bc it has logic to restart once it finds the value
    def odd_unique(self, arr, num):
        _sum=sum(arr)
        length = len(arr)
        if _sum<num:
            return 0
        if _sum==num:
            return length
        current=0
        best=length
        i=0
        start=0
        while i<len(arr):
            current+=arr[i]
            if current>=num:
                if len(arr[start:i+1])<best:
                    best=len(arr[start:i+1])
                start+=1
                i=start
                current=0
            else:
                i+=1
        return best

    def optimal(self, arr, num):
        _sum=sum(arr)
        if _sum<num:
            return 0
        if _sum==num:
            return arr
        l,r=0,-1
        #
        length=len(arr)
        length2=length
        _sum=0
        while l<length2:
            if _sum<num and r+1<length2:
                r+=1
                _sum+=arr[r]
            else:
                _sum-=arr[l]
                l+=1
            if _sum>=num:
                length=min(r-l+1, length)
        return length


def main():
    arr=[2, 3, 1, 2, 4, 3,7]
    num=7
    x = Solution().optimal(arr, num)
    print(x)

if __name__ == "__main__":
    main()