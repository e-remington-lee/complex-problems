# https://www.youtube.com/watch?v=0N_vjYKtx88

class Solution(object):
    def __init__(self):
        super().__init__()
        self.memoize = {}
        self.c=0
    
    def answer(self, n):
        if n <=2:
            return 1
        
        if n in self.memoize:
            return self.memoize[n]

        ans = 1*(n-1)
        for i in range(2, n):
            self.c+=1
            first = i
            second = n-i
            product = first*max(second, self.answer(second))
            if product > ans:
                ans = product
        
        # self.memoize[n]=ans
        return ans

def main():
    x = Solution()
    n=16
    print(x.answer(n))
    print(x.c)
    
# 7
# 5, 2
# 3, 2, 
# 1, 2

# 4, 3
# 2, 2,
# 0, 2

# 3 4
# 1 2 
# 0,1 

# 2 5
# 0 2
if __name__ == "__main__":
    main()

# threes, x=divmod(13-4, 3)
# print(3**threes*2*2)
# print(x,threes)



# Hints
# 
#
#
#
#
#
## O n^2 without optimal solution, constant space, O n with optimal and O n space
# Dynamic programming! remember what values you have already calculated and return those max values
# recursion, remember that you start a range(2,n) bc if it is less than 2, you return 1
#


