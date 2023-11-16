#TODO
# pre processing lists when you have a search function can reduce time complexity
# consider if a set is ideal but requires duplicaites, consider a hashmap

from collections import defaultdict

class Solution(object):
    def answer(self, magazine:list, word:str):
        for letter in word:
            if letter in magazine:
                magazine.remove(letter)
            else:
                return False
        return True

    def answer2(self, magazine:list, word:str):
        idxs = set()
        for letter in word:
            for letter_index in range(len(magazine)):
                if magazine[letter_index]==letter and letter_index not in idxs:
                    idxs.add(letter_index)     
                    if len(idxs) == len(word):
                        return True
        return False

    def answer3(self, magazine:list, word:str):
        if len(word)==0:
            return True
           
        l_map = defaultdict(int)
        for letter in magazine:
            if letter not in l_map:
                l_map[letter]=1
            else:
                l_map[letter]+=1
        
        for letter in word:
            if l_map[letter]==0:
                print(l_map)
                return False
            
            l_map[letter]-=1
            # try:
            #     if l_map[letter]==0:
            #         return False
            #     l_map[letter]-=1
            # except KeyError:
            #     return False
            # if letter in l_map and l_map[letter]>0:
            #     l_map[letter]-=1
            # else:
            #     return False
        return True

def main():
    magazine=["A", "B", "C", "D", "E", "F","F", "G"]
    word = "ABEDT"
    print(Solution().answer3(magazine, word))


main()