class Solution:
    def combine(self, n: int, k: int):          
        self.output=[]
        self.helper(n, k, 1, [])                
        return self.output
    
    def helper(self, n, k, index, temp):
        if len(temp)==k:
            self.output.append(temp[:])
        else:
            for j in range(index, n+1):
                temp.append(j)
                self.helper(n, k, j+1, temp)
                temp.pop()

    def using_modules(self, n, k):
        import itertools
        output=[]
        nums=range(1,n+1)
        combos = itertools.combinations(nums, k)
        for c in combos:
            output.append(list(c))
        return output


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)