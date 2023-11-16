from collections import defaultdict
import random
class Solution:
    def quick_select_solution(self, nums, k):
        self.frequency_dict = defaultdict(lambda: 0)
        for x in nums:
            self.frequency_dict[x] += 1
            
        self.keys = list(self.frequency_dict.keys())
            
        n = len(self.keys)
        
        self.quick_select(0, n - 1, n - k)
        
        return self.keys[n-k:]
        
            
    def partition(self, left, right, pivot):
        self.keys[pivot], self.keys[right] = self.keys[right], self.keys[pivot]
        # Remember that you need to use the RIGHT index NOT PIVOT since you just wapped pivot
        val = self.frequency_dict[self.keys[right]]
        low = left
        for i in range(left, right):
            if self.frequency_dict[self.keys[i]] < val:
                self.keys[i], self.keys[low] = self.keys[low], self.keys[i]
                low += 1
        self.keys[low], self.keys[right] = self.keys[right], self.keys[low]
        
        return low
    
    def quick_select(self, left, right, k):
        if left == right:
            return 
        
        pi = random.randint(left, right)
        pi = self.partition(left, right, pi)
        
        if pi == k:
            return 
        elif pi < k:
            return self.quick_select(pi + 1, right, k)
        else:
            return self.quick_select(left, pi - 1, k)


    def topKFrequent(self, nums, k: int):
        import heapq
        frequency_dict = defaultdict(lambda: 0)
        
        for x in nums:
            frequency_dict[x] += 1
        
        return heapq.nlargest(k, frequency_dict.keys(), frequency_dict.get)


    def my_custom_solution(self, nums, k):        
        frequency_dict = defaultdict(lambda: 0)
        
        for x in nums:
            frequency_dict[x] += 1
        
        response_key = []
        response_value = []
        for key, value in frequency_dict.items():
            index = self.binary_search(response_value, value)
            response_key.insert(index, key)
            response_value.insert(index, value)
        
        return response_key[-k:]
    

    def binary_search(self, arr, target):
        if len(arr) == 0:
            return 0
        low = 0
        high = len(arr) - 1
        while high >= low:
            mid = (high + low) // 2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)