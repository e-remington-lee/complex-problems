def oddEvenList(self, head):
        if not head:
            return None
        current = None
        odd = True
        odd_current = head
        even_head = even_current = head.next
        if even_current:
            current = even_current.next
        while current:
            if odd:
                odd_current.next = current
                odd_current = current
                odd = False
            else:
                even_current.next = current
                even_current = current
                odd = True
            current = current.next
        odd_current.next = even_head
        if even_current:
            even_current.next = None
        return head


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)