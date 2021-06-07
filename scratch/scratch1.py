class Solution:
    def answer(self, li, target):
        start=0
        stop=len(li)-1
        left = self.__find_left(start, stop, li, target)
        right = self.__find_right(start, stop, li, target)
        return [left, right]

    def __find_left(self, start, stop, li, target):
        if stop>=start:
            mid = (stop-start)//2+start
            if target<=li[mid]:
                if li[mid]==target and (target>li[mid-1] or mid==0):
                    return mid
                else:
                    return self.__find_left(start, mid-1, li ,target)
            else:
                return self.__find_left(mid+1, stop, li ,target)
        return -1
            
    def __find_right(self, start, stop, li, target):
        if stop>=start:
            mid = (stop-start)//2+start
            if target>=li[mid]:
                if li[mid]==target and (target<li[mid+1] or mid==len(li)-1):
                    return mid
                else:
                    return self.__find_right(mid+1, stop, li ,target)
            else:
                return self.__find_right(start, mid-1, li ,target)
        return -1

def main():
    li = [1,3,3,5,7,8,9,9,9,15]
    x=Solution()
    print(x.answer(li, 9))

main()




def fib(n):
    if n<=2:
        return 1
    first=0
    second=1
    for i in range(2, n+1):
        first, second = second, first+second
    return second

