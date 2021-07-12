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

'''
good example of object referecing in linked lists
slow.next = slow.next.next modifies slow, not head
but if slow.next=head, then we make slow=slow.next, then we make slow.next=3, that will modify head 2 bc slow/head point to same object
'''
class RemoveKthElement(object):
    def answer(self, head, n):
        #slow=fast=head DOES NOT WORK
        dummy=slow=fast=Node(0, head)
        for _ in range(n):
            fast=fast.next
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        '''
        this is because if we were to return the head itself, slow.next=head, but when we make slow.next=slow.next.next, we aren't modifying the head
        object, we are modifying the slow.next pointer.the slow.next pointer is what we want it to be, but head is NOT. we make the dummy object with
        dummy.next=head, we also do dummy=slow=fast, then when slow.next = new value, dummy.next = new value we want
        '''
        return dummy.next

n1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
x=RemoveKthElement()
y=x.answer(n1, 1)
print(y)

# 1, 2, 3, 4, 5, 6
# 4
# 1, 2, 4, 5, 6
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

'''
1. single pass does not mean 1 loop, it almost always means break up the loop and add more pointers/space
2. If you are 4 elements from the end of a linked list, you can loop through the linked list using a fast/slow pointer. the fast one goes forward 4 times, then we iterate through both until fast.next is None. This will give us the location of the index we need to remove
3. this is because both we are referring to the same linked list with the same length. 
4. if we are 4 from the end of a linked list of unknown length, we can node.next 4 times. When node1 is at its end, node2 will be at the 4th element from the end since we artificially set the end of node2 to node1, which is 4 shorter than original
'''