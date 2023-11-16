'''
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
  # Fill this in.
  
print staircase(4)
# 5
print staircase(5)
# 8

Can you find a solution in O(n) time?
'''
class Solution:
    # 1, 1, 2, 3, 5, 8, 13, 21
    def answer(self, steps: int):
        return self.fib(steps)
    
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
 
    def best(self, n):
        first=0
        second=1
        for _ in range(n):
            first, second = second, first+second
        return second

    def dynamic_programming(self, n: int) -> int:
        def helper(n, m):
            if n in m:
                return m[n]
            if n<=1:
                return 1
            x=helper(n-1, m)+helper(n-2, m)
            m[n]=x
            return x
        return helper(n, {})

def main():
    steps = 6
    response = Solution().answer(steps)
    resp2 = Solution().best(steps)
    print(response)
    print(resp2)
    import sys
    sys.path.append(".")
    from utilities import to_string
    flashcard=to_string.file_to_string(__file__)
    print(flashcard)

main()