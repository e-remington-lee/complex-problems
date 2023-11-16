class ListNode:
    def __init__(self, x, next = None, prev = None):
        self.val = x
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1 
        
        if index > self.size // 2:
            cur = self.tail
            for _ in range(self.size - index):
                cur = cur.prev
            return cur.val
        else:
            cur = self.head.next
            for _ in range(index):
                cur = cur.next
            return cur.val
    

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
            
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:      
        if index > self.size:
            return
        
        if index > self.size // 2:
            cur = self.tail
            for _ in range(self.size - index):
                cur = cur.prev
        else:
            cur = self.head.next
            for _ in range(index):
                cur = cur.next
        prev = cur.prev
        new = ListNode(val)
        prev.next = new
        new.prev = prev

        new.next = cur
        cur.prev = new
            
        self.size += 1
                           

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        
        if index > self.size // 2:
            cur = self.tail
            for _ in range(self.size - index):
                cur = cur.prev
        else:
            cur = self.head.next
            for _ in range(index):
                cur = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.size -= 1


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)
a='abc'
d ='dcezzz'
for x, y in zip(a, d):
    print(x,y)
from collections import Counter

m = Counter(d)
print(m['z'])
print(ord('z'))