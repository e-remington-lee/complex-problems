class ListNode(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

    def __str__(self):
        current=self
        li=[]
        while current:
            li.append(str(current.value))
            # print(current.value)
            current=current.next
        return "".join(li)

class Solution:
    def removeNthFromEnd(self, head, n):
        def get_length(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        l = get_length(head)
        if l == n:
            return head.next
        
        prev = None
        cur = head
        for _ in range(l - n):
            prev = cur
            cur = cur.next
        
        prev.next = cur.next
        return head

    def answer(self, head, n):
        dummy_head = ListNode(0, head)
        slow = fast = dummy_head
        for _ in range(n):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy_head.next

'''
good example of object referecing in linked lists
slow.next = slow.next.next modifies slow, not head
but if slow.next=head, then we make slow=slow.next, then we make slow.next=3, that will modify head 2 bc slow/head point to same object

this is because if we were to return the head itself, slow.next=head, but when we make slow.next=slow.next.next, we aren't modifying the head
object, we are modifying the slow.next pointer.the slow.next pointer is what we want it to be, but head is NOT. we make the dummy object with
dummy.next=head, we also do dummy=slow=fast, then when slow.next = new value, dummy.next = new value we want
'''


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
