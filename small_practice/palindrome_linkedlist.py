class Node(object):
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


class Palindrome(object):
    def answer(self, node):
        slow=fast=current=node
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        slow=self.reverse(slow)
        while slow:
            if slow.value!=current.value:
                return False
            slow=slow.next
            current=current.next
        return True
    
    def reverse(self, node):
        prev=None
        while node:
            _next=node.next
            node.next=prev
            prev=node
            node=_next
        return prev

    def answer_recursive(self, node):
        return self.helper(node, node, node, None)
       

    def helper(self, slow, fast, current, prev):
        if slow and fast and fast.next:
            if self.helper(slow.next, fast.next.next, current, prev):
                return True
        elif slow:
            _next=slow.next
            slow.next=prev
            prev=slow
            if self.helper(_next, fast, current, prev):
                return True
        elif prev:
            if prev.value!=current.value:
                return False
            elif self.helper(slow, fast, current.next, prev.next):
                    return True
        else:
            return True

    

n1 = Node(1, Node(2, Node(3, Node(2, Node(7)))))
n2 = Node(1, Node(2, Node(2, Node(2, Node(2, Node(1))))))
x=Palindrome()
print(x.answer_recursive(n2))
print(x.answer(n1))

# 1, 2, 3, 4, 5, 6
# 4
# 1, 2, 4, 5, 6
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
'''
1. to get to a midpoint of a linked list, perform slow=fast=node, while fast and fast.next. you need fast and fast.next bc on even linked lists, fast.next is valid but it will equal None, so None.next = NPE
2. slow points to the middle, the reverse of the middle will be equal to the current during a while loop for both, so while slow, check if current!=slow, if true return False, if not True
3. for recursive, we have to make sure each previous if/else statement is invalid when we hit the next one. the second if statement will change slow.next, which can affect the fast.next loop since we are changing the same objects in memory. we need to add if slow and fast and fast.next to prevent this, bc if slow==None, we won't have the first or second if loop
'''