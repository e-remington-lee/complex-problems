# TL;DR: You can't do relative imports from the file you 
# execute since __main__ module is not a part of a package.

from Subclass import Answer
from Easy.pythagorean_triplets import Solution

print(Solution().answer([1,2,3]))