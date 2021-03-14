class Solution:
    # 1, 1, 2, 3, 5, 8, 13, 21
    def answer(self, steps):
        return self.fib(steps)
    
    # TODO reverse engineer this to a better degree
    def fib(self, index):
        if index<=1:
            return 1
        return self.fib(index-1) + self.fib(index-2)
        # 5: 1 1 1 1 1, 1 2 1 1, 1 1 2 1, 1 1 1 2, 2 1 1 1, 2 2 1, 2 1 2, 1 2 2
        # 4: 1 1 1 1, 1 2 1, 2 1 1, 1 1 2, 2 2,
        # 3: 1 1 1, 2 1, 1 2

        # if index==0:
        #     return 1
        # elif index<0:
        #     return 0
        # else:
        #     return self.fib(index-1) + self.fib(index-2)

    def not_fib(self, index):
        if index==1:
            return 1
        # start at increment 2 bc index 0, 1 are accounted for already
        increment = 2
        response = 0
        last = 1
        second_last = 1
        while increment <= index:
            increment+=1
            response = last+second_last
            second_last=last
            last=response           

            # 1; r=1 -- l=1, sl=1
            # 2; r=2 -- sl=l=1, l=r=2
            # 3; r=3, sl=l=2, l=r=3
            # 4; r=5

        return response

from time import time  

def main():
    steps = 5
    t0 = time()
    response = Solution().answer(steps)
    t1 = time()
    resp2 = Solution().not_fib(steps)
    t2 = time()
    # response = Solution().fib(steps)
    print(response)
    print(t1)
    print(resp2)
    print(t2)

main()