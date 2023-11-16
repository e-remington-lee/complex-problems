from functools import lru_cache
import math
from utilities import flashcard

# flashcard(__file__)
import setuptools
print(setuptools.find_packages())

@lru_cache(None)
def compute_something(n):
    x=math.pow(n, n)
    return x

count=0
@lru_cache(maxsize=None)
def fib(n):
    global count
    count+=1
    # if n==0:
        # return 0
    ## depending on if we want the 0th index as 1 or 1 index as 1
    if n==1 or n==0:
        return 1
    return fib(n-1)+fib(n-2)
# 1 1 2 3 5 8 13
print(fib(10))
print(fib.cache_info())
print(count)
# compute_something(5)
# print(compute_something.cache_info())

# from javaPractice import permutations_lc as p
# print(p.Solution().permute([1,2,3]))
buildings = [[2,9,10],[5,12,12],[19,24,8], [3,7,15], [15,20,10]]
def sort(buildings, start, stop):
    if stop>=start:
        pi = partition(buildings, start, stop)
        sort(buildings, pi+1, stop)
        sort(buildings, start, pi-1)
    return buildings

def partition(buildings, start, stop):
    pivot = buildings[stop][0]
    low=start
    for i in range(start, stop):
        if pivot>=buildings[i][0]:
            buildings[i], buildings[low]=buildings[low], buildings[i]
            low+=1
    buildings[low], buildings[stop] = buildings[stop], buildings[low]
    return low

print(sort(buildings, 0, len(buildings)-1))
x_start, x_end, y = buildings[0]
print(x_start, x_end)


# r=[]


# x = [[1,2,3], [1,2,3]]
# y = x[:]
# x[0][0] = 5
# print(y)
# print(x)
# xx = [1,2,3]
# yy = xx[:]
# yy[0] = 5
# print(xx)
# print(yy)


# class Compared:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __lt__(self, other):
#         return self.y < other.y

# two= Compared(1, 2)
# five= Compared(1, 5)

# print(five<5)
# print(two<five)



