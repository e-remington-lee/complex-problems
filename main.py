# TL;DR: You can't do relative imports from the file you 
# execute since __main__ module is not a part of a package.

#Link https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x

from Subclass import Answer
from Easy.pythagorean_triplets import Solution

print(Solution().answer([1,2,3]))