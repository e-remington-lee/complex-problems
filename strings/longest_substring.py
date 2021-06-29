'''
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

s= "ppkwkew
'''
class Solution(object):
    def answer(self, s):
        map={}
        start=length=0
        for i,x in enumerate(s):
            if x in map and start<=map[x]:
                start=map[x]+1
            else:
                length=max(length, i-start+1)
            map[x]=i
        return length


def main():
    s="ppkwkew"
    x=Solution().answer(s)
    print(x)

if __name__=="__main__":
    main()