class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        self.__flatten_helper(head)
        return head
    
    def __flatten_helper(self, root):
        if not root:
            return root
        
        cur = root
        while cur and (cur.next or cur.child):
            if cur.child:
                hold = cur.next
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
                tail = self.__flatten_helper(cur.next)
                tail.next = hold
                if hold:
                    hold.prev = tail
                cur = tail
            else:
                cur = cur.next
        return cur

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)