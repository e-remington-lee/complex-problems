# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

# Example:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]

# Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

class Solution:
    def answer_brute(self, search, word):
        for y in range(len(search)):
            for x in range(len(search[0])):  
                row = self.row1(x, y, search, len(word))
                column = self.column1(x, y, search, len(word))
                if word in row or word in column:
                    return True
        return False                    
    
    @staticmethod
    def row1(x, y, search, word):
        return "".join([search[y][x] for x in range(x, len(search[0]))])[:word]

    def column1(self, x, y, search, word):
        return "".join([search[y][x] for y in range(y, len(search))])[:word]


    def answer1(self, search, word):
        for y in range(len(search)):
            for x in range(len(search[0])):
                if search[y][x] == word[0]:
                    if self.find_words_down(x,y,search,word):
                        return True
                    if self.find_words_side(x,y,search,word):
                        return True
        return False
        

    def find_words_down(self, x, y, search, word):
        word_len = len(word)
        # a b c d e f
        #     c  
        if word_len > len(search)-y:
            return False
        return "".join([search[y][x] for y in range(y, y+word_len)]) == word

    def find_words_side(self, x, y, search, word):
        word_len = len(word)
        # a b c d e f
        #     c  
        if word_len > len(search[0])-x:
            return False
        return "".join([search[y][x] for x in range(x, x+word_len)]) == word
        
                    
                    
def main():
    search=[
        ['A', 'F', "O", "A"],
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'X', 'S', 'S']]

    print(Solution().answer_brute(search, "FACU"))
    print(Solution().answer1(search, "OCQOS"))

main()


# notes The time complexity of this solution is O(N x M x k) where k is the length of the target word. This is because in the worst case, we are iterating through the entire 2D array which is N*M, and then constructing and checking for a match with the target word of length k.
