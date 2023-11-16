class Solution:
    def cleaner(self, flowerbed, n):
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False

    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                back = False
                forward = False
                if i - 1 >= 0:
                    if flowerbed[i - 1] != 1:
                        back = True
                else: 
                    back = True
                    
                if i + 1 < len(flowerbed):
                    if flowerbed[i + 1] != 1:
                        forward = True
                else:
                    forward = True
                if forward and back:
                    n -= 1
                    flowerbed[i] = 1
                if n == 0:
                    return True
        return False

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)