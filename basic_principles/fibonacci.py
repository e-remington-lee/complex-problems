class Fib:
    def recurrsive_fib1(self, n):
        if n <=1:
            return 1
        return self.recurrsive_fib1(n-1) + self.recurrsive_fib1(n-2)

    def fib(self, n):
        #index 0, 1, 2 are 1,1,2 vs indexing at 1,2,3 as 1,1,2
        first=0
        second=1
        for _ in range(n):
            first, second = second, first+second
        return second

    
print(Fib().recurrsive_fib1(4))
print(Fib().fib(4))

