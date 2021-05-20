class Solution:
    def answer(self, word, search):
        for i, y in enumerate(search):
            for j, x in enumerate(search[i]):
                if x==word[0]:
                    if self.__helper_right(word, search, i, j):
                        return True
                    elif self.__helper_down(word,search, i, j):
                        return True
        return False

    def __helper_right(self, word, search,i, j):
        l=len(word)
        for ii, x in enumerate(search[i][j:]):
            if l<=len(search[i][ii:]):
                searched_word = "".join(search[i][ii:ii+l])
                if searched_word==word:
                    return True
        return False

    def __helper_down(self, word, search, i, j):
        l=len(word)
        li=[]
        if l<=len(search[i:]):
            for ii in range(l):
                li.append(search[i+ii][j])
            if word=="".join(li):
                return True
        return False



def main():
    search = [['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S']]
    x=Solution()
    print(x.answer("CQOB", search))


main()