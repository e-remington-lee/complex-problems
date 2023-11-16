import heapq
from collections import defaultdict, Counter


class Solution:
    def kLogN(self, words, k):
        frequency = Counter(words)
        heap = []
        for word, freq in frequency.items():
            heap.append(Comparator(freq, word))
        
        heapq._heapify_max(heap)
        return [str(heapq._heappop_max(heap)) for _ in range(k)]


    def NlogK(self, words, k):
        frequency = Counter(words)
        # frequency = defaultdict(int)
        # for word in words:
            # frequency[word] += 1
        heap = []
        for word, freq in frequency.items():
            heap.append(Comparator(freq, word))
        
        response = heapq.nlargest(k, heap)
        return [str(x) for x in response]
            
            
class Comparator:
    def __init__(self, count, letter):
        self.count = count
        self.letter = letter
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.letter > other.letter
        return self.count < other.count
    
    def __str__(self):
        return str(self.letter)

print(Solution().kLogN(["i","love","leetcode","i","love","coding"], 2))

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

heap = []
heap.append(Comparator(6, "a"))
heap.append(Comparator(3, "b"))
heap.append(Comparator(3, "d"))
heapq._heapify_max(heap)
print(heapq._heappop_max(heap))
print(heapq._heappop_max(heap))
print(heapq._heappop_max(heap))