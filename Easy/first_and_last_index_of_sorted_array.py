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