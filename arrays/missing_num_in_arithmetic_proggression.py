class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        
        diff = (arr[n - 1] - arr[0]) // n
        low = 0
        high = n - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if (arr[mid] == arr[0] + mid * diff):
                low = mid + 1
            else:
                high = mid
                
        return arr[0] + high * diff

a = ['a']
print(a[0].upper())