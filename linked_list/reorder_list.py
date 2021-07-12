class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class Solution:
    def brute(self, head) -> None:
        if not head:
            return head
        m={}
        l=1
        c=head.next
        while c:
            m[l]=c
            l+=1
            c=c.next
        count=key=1
        trigger=True
        c=head
        while count < l:
            if trigger:
                c.next=m[l-key]
                trigger = not trigger
            else:
                c.next=m[key]
                trigger=not trigger
                key+=1
            c=c.next
            count+=1
        c.next=None
        return head

    def optimal(self, head):
        if not head:
            return head
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        while slow:
            n=slow.next
            slow.next=prev
            prev=slow
            slow=n
        while prev.next:
            hold1=head.next
            head.next=prev
            head=hold1
            hold2=prev.next
            prev.next=head
            prev=hold2
            # head.next, head = prev, head.next
            # prev.next, prev = head, prev.next        
        # return new.next

n1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))   
x=Solution()
print(x.optimal(n1))