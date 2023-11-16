
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        if not head:
            new = Node(insertVal)
            new.next = new
            return new
        # this is not needed, bc we check for it later, but honestly it was good to have at the time before I realized 
        # the values could all be the same
        if not head.next:
            new = Node(insertVal)
            head.next = new
            new.next = head
            return head
        
        cur = head.next
        prev = head
        while True:
            if cur.val >= prev.val:
                if prev.val <= insertVal <= cur.val:
                    new = Node(insertVal)
                    prev.next = new
                    new.next = cur
                    break
            else:
                if prev.val <= insertVal or cur.val >= insertVal:
                    new = Node(insertVal)
                    prev.next = new
                    new.next = cur
                    break
                        
            if cur == head:
                new = Node(insertVal)
                prev.next = new
                new.next = cur
                break
            prev = cur
            cur = cur.next
        
        return head


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)