class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        

    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1 
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
        
        cur = self.head.next
        prev = self.head
        for _ in range(index):
            prev = cur
            cur = cur.next
        
        new = ListNode(val)
        prev.next = new
        new.next = cur
        self.size += 1
                           

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        
        cur = self.head.next
        prev = self.head
        for _ in range(index):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        self.size -= 1

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        index += 1
        cur = self.head
        while index > 0 and cur:
            cur = cur.next
            index -= 1
        return -1 if not cur else cur.val

    def addAtHead(self, val: int) -> None:
        hold = self.head.next
        _new = ListNode(val)
        self.head.next = _new
        _new.next = hold

    def addAtTail(self, val: int) -> None:
        cur = self.head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
        prev.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            index += 1
            cur = self.head
            prev = None
            while index > 0 and cur:
                prev = cur
                cur = cur.next
                index -= 1

            if index == 0:
                if not cur:
                    prev.next = ListNode(val)
                else:
                    _new = ListNode(val)
                    prev.next = _new
                    _new.next = cur          

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            index += 1
            cur = self.head
            prev = None
            while index > 0 and cur:
                prev = cur
                cur = cur.next
                index -= 1
                
            if index == 0 and cur:
                prev.next = cur.next


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)