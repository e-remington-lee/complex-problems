'''
https://www.section.io/engineering-education/heap-data-structure-python/
'''
class MaxHeap:
    def __init__(self):
        # Initialize a heap using list
        self.heap = []

    def getParentPosition(self, i):
        # The parent is located at floor((i-1)/2)
        return int((i-1)/2)

    def getLeftChildPosition(self, i):
        # The left child is located at 2 * i + 1
        return 2*i+1

    def getRightChildPosition(self, i):
        # The right child is located at 2 * i + 2
        return 2*i+2

    def hasParent(self, i):
        # This function checks if the given node has a parent or not
        return self.getParentPosition(i) < len(self.heap)

    def hasLeftChild(self, i):
        # This function checks if the given node has a left child or not
        return self.getLeftChildPosition(i) < len(self.heap)

    def hasRightChild(self, i):
        # This function checks if the given node has a right child or not
        return self.getRightChildPosition(i) < len(self.heap)

    def insert(self, key):
        self.heap.append(key) # Adds the key to the end of the list
        self.heapify(len(self.heap) - 1) # Re-arranges the heap to maintain the heap property

    def getMax(self):
        return self.heap[0] # Returns the largest value in the heap in O(1) time.

    def heapify(self, i):
        while(self.hasParent(i) and self.heap[i] > self.heap[self.getParentPosition(i)]): # Loops until it reaches a leaf node
            self.heap[i], self.heap[self.getParentPosition(i)] = self.heap[self.getParentPosition(i)], self.heap[i] # Swap the values
            i = self.getParentPosition(i) # Resets the new position

    def printHeap(self):
        print(self.heap) # Prints the heap

import heapq

x= [9,12,16,5,12,7]
print(heapq.heapify(x))
print(x)
print(heapq.nsmallest(2, x))

x = 1412034124132
y = 1412034124132
print(x is y)