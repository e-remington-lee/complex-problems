# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

class Solution:
    def answer(self, arr, target):
        low = 0
        high = len(arr)-1
        # last = self.get_last(arr, low, high, target)
        first = self.get_first(arr, low, high, target)
        last = self.get_last(arr, low, high, target)
        return [first, last]

    def get_first(self, arr, low, high, target):
        if (high >= low):
            mid = low + (high-low) // 2
            if (mid==0 or target > arr[mid-1]) and arr[mid]==target:
                return mid
            elif target > arr[mid]:
                return self.get_first(arr, mid+1, high, target)
            else:
                return self.get_first(arr, low, mid-1, target)
        else:
            return -1

    def get_last(self, arr, low, high, target):
        if high >= low:
            mid = low + (high-low) // 2
            if (mid==len(arr)-1 or target < arr[mid+1]) and arr[mid]==target:
                return mid
            elif target >= arr[mid]:
                return self.get_last(arr, mid+1, high, target)
            else:
                return self.get_last(arr, low, mid-1, target)
        else:
            return -1

        

def main():
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 1
    ans = Solution().answer(arr, target)
    print(ans)

main()