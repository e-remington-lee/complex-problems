class Solution:
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        up = False
        down = False
        prev = arr[0]
        for x in arr[1:]:
            if x > prev and not down:
                up = True
            elif x < prev and up:
                down = True
            else:
                return False
            prev = x
        return down
                
                
    def while_loop(self, arr):
        if len(arr) < 3:
            return False
        end = len(arr)
        start = 0
        
        while start < end - 1 and  arr[start] < arr[start + 1]:
            start += 1
        
        if start == 0 or start == end - 1:
            return False
        
        while start < end -1 and arr[start] > arr[start + 1]:
            start += 1
            
        return start == end - 1

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)