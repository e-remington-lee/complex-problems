class WordBreak(object):
    '''
    Time complexity : O(2^n). Given a string of length n, there are about n ways to split it into two parts. 
    At each step, we have a choice: to split or not to split. In the worse case, 
    when all choices are to be checked, that results in O(2^n). This is because we split each word into 2, then each word in that into 2
    , and so on, 
    recognize that each entry can propogate into many more entries, and if they all do not return anything we have to go back to the start,
    increment 1, and do it again, these are usually exponential in some fashion

    Space complexity : O(n). The depth of the recursion tree can go upto n.
    '''
    def brute(self, s, wordDict):
        wd = set(wordDict)
        self.memo={}
        return self.brute_helper(s, wd, 0)

    def brute_helper(self, s, wordDict, start):
        if len(s)==start:
            return True
        for i in range(start+1, len(s)+1):
            if s[start:i] in wordDict and self.brute_helper(s, wordDict, i):
                    return True
        return False

    '''
    time: o n^3, n searches the initial string, and the recurion tree can become n^2, we reduce this from exponential because
    each combination of the strings will only be hit once bc of the memo
    in theory, n because we search the initial string, and n^2 because we have to search that string for each of its combinations
    at each charater, so n*n^2 = n^3

    space: o n, bc the recursion depth is only going to be the length of the initial string
    '''
    def answer1(self, s, wordDict):
        wd = set(wordDict)
        self.memo=[None]*len(s)
        return self.answer1_helper(s, wd, 0)

    def answer1_helper(self, s, wordDict, start):
        if start == len(s):
                return True
        if self.memo[start] is not None:
            return self.memo[start]
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.answer1_helper(s, wordDict, end):
                self.memo[start]=True
                return True
        self.memo[start]=False
        return False

        
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)

x = WordBreak()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(x.answer1(s, wordDict))