class Solution:
    def equal_sizes(self, arr1, arr2):
        output=[]
        p1,p2 = 0,0
        while p1<len(arr1) and p2<len(arr2):
            if arr1[p1] is arr2[p2]:
                output.append(arr1[p1])
                p1+=1
                p2+=1
            elif arr1[p1] < arr2[p2]:
                p1+=1
            else:
                p2+=1
        return output

    def not_equal_sizes(self, arr1, arr2):
        if len(arr1)<len(arr2):
            small=arr1
            larger=arr2
        else:
            large=arr1
            small=arr2
        output=[]
        for x in small:
            if self.binary_search(x, large):
                output.append(x)
        return output

    def binary_search(self, target, arr):
        low=0
        high=len(arr)-1
        while high>=low:
            mid = (high+low)//2
            if arr[mid] == target:
                return True
            elif target < arr[mid]:
                high=mid-1
            else:
                low=mid+1
        return False

def helper(arr, low, high, target):
    if high >= low:
        mid = (high+low) // 2
        if arr[mid] is target:
            return True
        elif arr[mid] < target:
            return helper(arr, mid+1, high, target)
        else:
            return helper(arr, low, mid-1, target)
    return False

def bs(arr, target):
    return helper(arr, 0, len(arr)-1, target)


def answer2(a1, a2):
    if len(a1) > len(a2):
        larger = a1
        smaller = a2
    else:
        larger = a2
        smaller = a1

    output = []
    for x in smaller:
        if bs(larger, x):
            output.append(x)
    return output

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(answer2(arr1, arr2))
x = Solution()
print(x.not_equal_sizes(arr1, arr2))
'''
time for one is MUCH larger than the other, N log(n), space=output array (constant)
time for they are equal, O(n+m) since worst case we traverse through both of the javaPractice fully, space is output  (constant)
'''
# import sys
# sys.path.append(".")
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)