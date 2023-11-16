import random

import random
import heapq
class Solution:
    def heapq(self, nums, k):
        # nlargest returns descending order [3, 2, 1]
        return heapq.nlargest(k, nums)[-1]
        
    def findKthLargest(self, nums, k):
        N = len(nums)
        kth_largest = N - k
        return self.quick_select(nums, 0, N - 1, kth_largest)
    
    def quick_select(self, arr, low, high, target):
        if high == low:
            return arr[low]
        
        pi = self.partition(arr, low, high)
        if pi == target:
            return arr[pi]
        elif pi > target:
            return self.quick_select(arr, low, pi - 1, target)
        else:
            return self.quick_select(arr, pi + 1, high, target)
        
    
    def partition(self, arr, low, high):
        pivot = random.randint(low, high)
        arr[pivot], arr[high] = arr[high], arr[pivot]
        pivot_value = arr[high]
        partition_index = low
        
        for i in range(low, high):
            if arr[i] < pivot_value:
                arr[i], arr[partition_index] = arr[partition_index], arr[i]
                partition_index += 1
        
        arr[partition_index], arr[high] = arr[high], arr[partition_index] 
        return partition_index


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)

l = [4, 1,2,3]
print(heapq.nsmallest(2, l))