class Fib:
    def recurrsive_fib1(self, n):
        if n <=1:
            return 1
        return self.fib1(n-1) + self.fib1(n-2)

    def iterative_fib(self, n):
        if n==0:
            return 0
        elif n<=2: 
            return 1
        index = 3
        first = 1
        second = 1
        response = 0
        while index <= n:
            index +=1
            response = first+second
            second = first
            first = response
        
        return response
    
print(Fib().iterative_fib(8))