from collections import defaultdict
class Solution:
    def arrangeWords(self, text: str) -> str:
        hashmap = defaultdict(list)
        response = []
        
        for word in text.split():
            hashmap[len(word)].append(word)
            
        for length in sorted(hashmap.keys()):
            for word in hashmap[length]:
                if not response:
                    tl = list(word)
                    tl[0] = tl[0].upper()
                    s = "".join(tl)
                    response.append(s)
                else:
                    response.append(word.lower())
        
        return " ".join(response)