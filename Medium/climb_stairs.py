class Solution:
    def answer(self, steps):
        answer = 0
        # 1, 1, 2, 3, 5, 8, 13, 21
        return answer
    
    # TODO reverse engineer this to a better degree
    def fib(self, index):
        if index==0:
            return 1
        elif index<0:
            return 0
        else:
            return self.fib(index-1) + self.fib(index-2)

def main():
    steps = 5
    # response = Solution().answer(steps)
    response = Solution().fib(steps)
    print(response)

main()