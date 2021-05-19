class Solution(object):
    def fib(self, num):
        # counts 0 as 0, 1 as the first 
        # if num==0:
        #     return 0
        if num==0:
            return 1
        elif num==1:
            return 1
        return self.fib(num-1)+self.fib(num-2)


    def answer(self, num):
        if num==0:
            return 0
        l1=0
        l2=1
        count=0
        while num > 0:
            hold = l1+l2
            l1=l2
            l2=hold
            num-=1
            count+=1
        return l2

    def a2(self, num):
        if num==0:
            return 0
        a, b = 1, 0
        for i in range(num):
            a, b = a+b, a
        return a
    

        
def main():
    arr = [3, 3, 2, 1, 3, 2, 1]
    x = Solution().answer(5)
    print(x)
main()