from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        response = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            response[tuple(count)].append(word)
        
        return response.values()