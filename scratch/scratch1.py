class Solution:
    def answer(self):
        pass

def fib(n):
    if n<=2:
        return 1
    first=0
    second=1
    for i in range(2, n+1):
        first, second = second, first+second
    return second
    

print(fib(3))

def main():
    x=Solution()
    print(x.answer())

main()