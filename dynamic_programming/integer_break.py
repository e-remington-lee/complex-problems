'''
https://www.youtube.com/watch?v=0N_vjYKtx88
https://leetcode.com/problems/integer-break/
'''
class IntegerBreak(object):
    def answer(self, n):
        #if 0, return 0
        if n<=1:
            return 0
        elif n==2:
            return 1
        elif n==3:
            return 2
        return self.answer_helper(n, {})

    def answer_helper(self, i, hm):
        if i==0 or i==1:
            return 1
        elif i==2:
            return 2
        elif i==3:
            return 3
        elif i in hm:
            return hm[i]
        best=i-1
        for t in range(2, i):
            best=max(best, t*self.answer_helper(i-t, hm))
        hm[i]=best
        return best

    # def __init__(self):
    #     super().__init__()
    #     self.memoize = {}
    #     self.c=0
    
    # def answer(self, n):
    #     if n <=2:
    #         return 1
        
    #     if n in self.memoize:
    #         return self.memoize[n]

    #     ans = 1*(n-1)
    #     for i in range(2, n):
    #         self.c+=1
    #         first = i
    #         second = n-i
    #         product = first*max(second, self.answer(second))
    #         if product > ans:
    #             ans = product
        
    #     self.memoize[n]=ans
    #     return ans

def main():
    x = IntegerBreak()
    n=16
    print(x.answer(n))
    print(x.c)

if __name__ == '__main__':
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


