from collections import deque
class Solution:
    def factory(self, s):
        return " ".join(reversed(s.split()))
        '''
        s ="b".join("ac") = abc
        s ="b".join("a") = a
        print(s)
        '''

    def optimized_linear_solution(self, s):
        if not s:
            return ""
        
        response = deque()
        start = 0
        in_word = False
        for i in range(len(s)):
            if s[i] != " ":
                if not in_word:
                    start = i
                    in_word = True
            elif in_word:
                response.appendleft(s[start:i])
                in_word = False
        
        if in_word:
            response.appendleft(s[start:])

        return " ".join(response)


    '''
    I got this my first try! worked and everything, but not optimized bc we add spaces after the fact intsead of during
    '''
    def linear_not_optimized(self, s):
        if not s:
            return ""
        
        response = deque()
        start = 0
        in_word = False
        for i in range(len(s)):
            if s[i] != " ":
                if not in_word:
                    start = i
                    in_word = True
            elif in_word:
                response.appendleft(s[start:i])
                in_word = False
        
        if in_word:
            response.appendleft(s[start:])

        response2 = []
        for j in range(len(response)):
            if j == len(response) - 1:
                response2.append(response[j])
            else:
                response2.append(response[j] + " ")
        
        return "".join(response2)

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
