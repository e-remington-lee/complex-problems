#https://leetcode.com/problems/linked-list-cycle/solution/
class Node:
    def __init__(self, x, n=None, tim=3):
        self.val = x
        self.next = n
class Solution:
    def is_cyclic(self, node):
        slow=fast=node
        while slow and fast and fast.next:
            if slow.next is fast.next.next:
                return True
            slow=slow.next
            fast=fast.next.next
        return False

    def base(self, node):
        m={}
        current=node
        while current:
            if current in m:
                return True
            m[current]=True
            current=current.next

        return False

    def recursive(self, head: Node) -> bool:
        if not head or not head.next:
            return False
        return self.helper(head, head)
    
    def helper(self, slow, fast):
        if not slow or not fast or not fast.next:
            return False
        if slow.next is fast.next.next:
            return True
        elif self.helper(slow.next, fast.next.next):
            return True

    


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

'''
Intuition

Imagine two runners running on a track at different speed. What happens when the track is actually a circle?

Algorithm

The space complexity can be reduced to O(1)O(1) by considering two pointers at different speed - a slow pointer and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two steps at a time.

If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.

Now consider a cyclic list and imagine the slow and fast pointers are two runners racing around a circle track. The fast runner will eventually meet the slow runner. Why? Consider this case (we name it case A) - The fast runner is just one step behind the slow runner. In the next iteration, they both increment one and two steps respectively and meet each other.

How about other cases? For example, we have not considered cases where the fast runner is two or three steps behind the slow runner yet. This is simple, because in the next or next's next iteration, this case will be reduced to case A mentioned above.
'''