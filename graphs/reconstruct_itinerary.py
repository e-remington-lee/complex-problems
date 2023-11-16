from collections import defaultdict
import random

class Solution:
    def findItinerary(self, tickets):
        self.target_length = len(tickets) + 1
        self.graph = defaultdict(list)
        self.seen = defaultdict(list)
        for start, destination in tickets:
            # index = self.binary_insert(graph[start], destination)
            self.graph[start].append(destination)
            self.seen[start].append(False)
            
        for start, destinations in self.graph.items():
            self.qs(destinations, 0, len(destinations) - 1)
            # destinations.sort() # qs, bubble sort, heap sort, merge sort
        
        self.response = []
        self.graph_search("JFK", ["JFK"])
        return self.response
    
    
    def graph_search(self, current, carry_list):
        if len(carry_list) == self.target_length:
            self.response = list(carry_list)
            return True

        for i in range(len(self.graph[current])):
            if not self.seen[current][i]:
                dest = self.graph[current][i]  
                self.seen[current][i] = True
                carry_list.append(dest)
                done = self.graph_search(dest, carry_list)     
                self.seen[current][i] = False
                carry_list.pop()
                if done:
                    return True
        return False
    
    def qs(self, arr, left, right):
        if right >= left:
            pi = self.partition(arr, left, right)
            self.qs(arr, left, pi - 1)
            self.qs(arr, pi + 1, right)
            
    def partition(self, arr, left, right):
        pivot_index = random.randint(left, right)
        arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
        pivot = arr[right]
        low = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[low], arr[i] = arr[i], arr[low]
                low += 1
        arr[right], arr[low] = arr[low], arr[right]
        return low


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)