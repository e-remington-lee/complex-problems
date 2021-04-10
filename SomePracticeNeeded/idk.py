class Solution:
    def classic(self, s):
        li = list(s)
        i, j = 0, len(s)-1
        while i <= j:
            li[i], li[j] = li[j], li[i]
            i+=1
            j-=1
        return "".join(li)

    def pythonic(self, s):
        return s[::-1]


print(Solution().classic("hello"))
print(Solution().pythonic("hello"))

