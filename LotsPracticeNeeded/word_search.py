# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

# Example:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]

# Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

class Solution:
    def answer1(self, search, word):
        for row in search:
            if word[0] in row:
                searching = True
                word_len = len(word)
                while searching:
                    idx = row.index(word[0])
                    ss_right = True
                    ss_left = True
                    right_idx = 1
                    left_idx = 1
                    while idx+right_idx<=len(row)-1 and ss_right==True:
                        if row[idx+right_idx]==word[right_idx]:
                            if right_idx==word_len-1:
                                return True
                            right_idx+=1
                        else:
                            ss_right=False
                    searching = False
                    
                    
                    
                    





def main():
    search=[
        ['A', 'F', "O", "A", "M", "X", "y"],
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]

    print(Solution().answer1(search, "FOAM"))

main()