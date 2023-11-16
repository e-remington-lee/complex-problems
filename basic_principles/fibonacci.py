class Fib:
    def recurrsive_fib1(self, n):
        if n <=1:
            return n
        return self.recurrsive_fib1(n-1) + self.recurrsive_fib1(n-2)
    
    # change from return first to return second if you want index based on 0th vs 1st.
    def fib(self, n):
        #index 0, 1, 2 are 1,1,2 vs indexing at 1,2,3 as 1,1,2
        first=0
        second=1
        for _ in range(n):
            first, second = second, first+second
        return first

    # change from return n to return 1 if you want index based on 0th vs 1st.
    def fib_memo(self, n):
        def helper(n, m):
            if n in m:
                return m[n]
            if n<=1:
                return n
            x=helper(n-1, m)+helper(n-2, m)
            m[n]=x
            return x
        return helper(n, {})
    
print(Fib().recurrsive_fib1(4))
print(Fib().fib(4))
print(Fib().fib_memo(4))


n=[2, 5, 3, 7, 6, 8]
t=2
import heapq

print(heapq.heapify(n))
print(n)
heapq.heappush(n, 4)
print(n)
heapq.heappop(n)
print(n)
heapq.heappop(n)

print(n)
heapq.heappop(n)

print(n)
# print(heapq.nlargest(t, n))
import random
print(random.randint(1,2))