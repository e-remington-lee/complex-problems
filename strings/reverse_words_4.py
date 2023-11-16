'''
You are given a character array containing a set of words separated by whitespace.

Your task is to modify that character array so that the words all appear in reverse order.

Do this without using any extra space.

There can be trailing spaces and more spaces in between the words
'''

class Solution:
    def answer(self, input):
        self.remove_trailing_leading_spaces(input)
        self.remove_inside_spaces(input)
        return self.reverse_words(input)

    def remove_inside_spaces(self, input):
        first_white_space = False
        for i in range(len(input) -1, -1, -1):
            if input[i] == " ":
                if first_white_space:
                    del input[i]
                else:
                    first_white_space = True
            else:
                first_white_space = False

    def remove_trailing_leading_spaces(self, input):
        while input[-1] == " ":
            input.pop()
        input.reverse()
        while input[-1] == " ":
            input.pop()
        input.reverse()
    
    def reverse_words(self, input):
        input = input[::-1]
        start = 0
        in_word = False
        for i in range(len(input)):
            if input[i] != " ":
                if not in_word:
                    start = i
                    in_word = True
                
            elif in_word:
                self.reverse(start, i, input)
                in_word = False
        
        if in_word:
            self.reverse(start, len(input), input)
        return input

    
    def reverse(self, start, stop, input):
        stop -= 1
        while stop > start:
            input[start], input[stop] = input[stop], input[start]
            start += 1
            stop -= 1

input = [' ', 'A', 'l', 'i', 'c', 'e', ' ', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'B', 'o', 'b', ' ']
expected = ['B', 'o', 'b', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'A', 'l', 'i', 'c', 'e']
x = Solution().answer(input)
print(input)
print(x)
assert x == expected 

li= [1,1,2,3,4, 1, 5, 1]
for i in range(len(li) -1, -1, -1):
    print(i)
    if li[i] == 1:
        del li[i]

print(li)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)