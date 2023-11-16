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
        # last = self.last_index(arr, low, high, target)
        first = self.first_index(arr, low, high, target)
        last = self.last_index(arr, low, high, target)
        return [first, last]

    def first_index(self, arr, low, high, target):
        if high>=low:
            mid = low+(high-low)//2
            if (mid==0 or target > arr[mid-1]) and arr[mid]==target:
                return mid
            elif target <= arr[mid]:
                return self.first_index(arr, low, mid-1, target)
            else:
                return self.first_index(arr, mid+1, high, target)
        return -1

    def last_index(self, arr, low, high, target):
        if high>=low:
            mid = (high-low)//2 +low
            if (mid==len(arr)-1 or target<arr[mid+1]) and target==arr[mid]:
                return mid
            if target>=arr[mid]:
                return self.last_index(arr, mid+1, high, target)
            else:
                return self.last_index(arr, low, mid-1, target)
        return -1


    # def __find_left(self, start, stop, li, target):
    #     if stop>=start:
    #         mid = (stop-start)//2+start
    #         if target<=li[mid]:
    #             if li[mid]==target and (target>li[mid-1] or mid==0):
    #                 return mid
    #             else:
    #                 return self.__find_left(start, mid-1, li ,target)
    #         else:
    #             return self.__find_left(mid+1, stop, li ,target)
    #     return -1
            
    # def __find_right(self, start, stop, li, target):
    #     if stop>=start:
    #         mid = (stop-start)//2+start
    #         if target>=li[mid]:
    #             if li[mid]==target and (target<li[mid+1] or mid==len(li)-1):
    #                 return mid
    #             else:
    #                 return self.__find_right(mid+1, stop, li ,target)
    #         else:
    #             return self.__find_right(start, mid-1, li ,target)
    #     return -1

        

def main():
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 2
    ans = Solution().answer(arr, target)
    print(ans)
    print(__file__)
    import sys
    sys.path.append(".")
    from utilities import to_string
    flashcard=to_string.file_to_string(__file__)
    print(flashcard)

main()