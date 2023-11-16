from itertools import combinations

'''
LC hard problem
'''
class LongestCommonSequence(object):  
    '''
    time, space = 2^n, 2^n is the number of subsequences for a given object
    '''    
    def brute(self, t1, t2):
        s1 = self.all_subsequences(t1)
        s2 = self.all_subsequences(t2)
        m=0
        for x in s1:
            if x in s2:
                m=max(m, len(x))
        return m

    def all_subsequences(self, s):
        out = set()
        for r in range(1, len(s) + 1):
            for c in combinations(s, r):
                out.add(''.join(c))
        return out

    '''
    time O (M*N^2), it takes N*M iterations to go throug both strings, but we do string2.find(char, int)
    space: n*m bc of memo
    '''
    def answer1(self, t1, t2):
        self.memo = [[-1 for x in t1] for y in t2]
        self.t1=t1
        self.t2=t2
        return self.answer1_helper(0,0)
    
    def answer1_helper(self, p1, p2):
        if p1==len(self.t1) or p2==len(self.t2):
            return 0

        if self.memo[p2][p1] !=-1:
            return self.memo[p2][p1]
        option1=self.answer1_helper(p1+1, p2)
        fo=self.t2.find(self.t1[p1], p2)
        option2=0
        if fo!=-1:
            option2=1+self.answer1_helper(p1+1, fo+1)
        self.memo[p2][p1]=max(option1, option2)
        return self.memo[p2][p1]

    '''
    time: O(N*M), the length of both strings
    space: O(n*m), the grid
    '''
    def dynamic_programming_memo(self, t1, t2):
        self.memo = [[-1 for x in t1] for y in t2]
        self.t1=t1
        self.t2=t2
        return self.answer2_helper(0,0)

    def answer2_helper(self, p1, p2):
        if len(self.t1)==p1 or len(self.t2)==p2:
            return 0
        if self.memo[p2][p1] != -1:
            return self.memo[p2][p1]
        
        if self.t1[p1]==self.t2[p2]:
            option=1+self.answer2_helper(p1+1, p2+1)
        else:
            option=max(self.answer2_helper(p1+1, p2), self.answer2_helper(p1, p2+1))
        self.memo[p2][p1]=option
        return option

    def prevent_out_of_index_errors(self, text1, text2):
        row = len(text1) - 1
        col = len(text2) - 1
        grid = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for row in range(len(text1) -1, -1, -1):
            for col in range(len(text2) - 1, -1, -1):
                if text2[col] == text1[row]:
                    grid[row][col] = grid[row + 1][col + 1] + 1
                else:
                    grid[row][col] = max(grid[row][col + 1], grid[row + 1][col])
        return grid[0][0]

    '''
    time: O(N*M), the length of both strings
    space: O(2*m), the length of both lists
    '''
    def optimized_space_reverse_list(self, text1, text2):
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        len_t2 = len(text2)
        current = [0] * (len_t2 + 1)
        prev = [0] * (len_t2 + 1)
        for row in range(len(text1) -1, -1, -1):
            for col in range(len(text2) - 1, -1, -1):
                if text1[row] == text2[col]:
                    current[col] = prev[col + 1] + 1
                else:
                    current[col] = max(current[col + 1], prev[col])
            prev, current = current, prev
        return prev[0]

    '''
    time: O(N*M), the length of both strings
    space: O(2*m), the length of both lists
    '''
    def optimized_space(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        cur, prev = [0] * (len(text2) + 1), [0] * (len(text2) + 1)
        
        for row in range(1, len(text1) + 1):
            for col in range(1, len(text2) + 1):
                # this helps us with the out of index error while properly indexing the strings
                if text1[row - 1] == text2[col - 1]:
                    cur[col] = prev[col - 1] + 1
                else:
                    cur[col] = max(cur[col - 1], prev[col])
            prev, cur = cur, prev
        return prev[-1]

# Below is the implementation of the above approach
def printSubsequence(input, output="", response=set()):
    # Base Case
    # if the input is empty print the output string
    if len(input) == 0:
        if output:
            response.add(output)
        return 
     
    # output is passed with including the
    # 1st characther of input string
    printSubsequence(input[1:], output+input[0])
 
    # output is passed without including the
    # 1st character of input string
    printSubsequence(input[1:], output)
    return sorted(response)

x = LongestCommonSequence()
# t1="taexta"
# t2="abtet"
t1="abcba"
t2="abcbcba"
print(x.previous_row(t1, t2))
#Answer4/3 is probably good enough tbh
print(x.full_grid(t1, t2))
print("1234".find("1", 2))
s='abcdefg'
li=set()
for i in range(1, len(s)+1):
    x=combinations(s,i)
    for j in x:
        li.add("".join(j))
print(li)

res = [s[x:y] for x, y in combinations(
            range(len(s) + 1), r = 2)]
response=[]
for i in range(len(s)):
    si=[]
    for j in range(i, len(s)):
        si.append(s[j])
        response.append("".join((si)))
print(res)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)