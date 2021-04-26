class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, head=None):
        super().__init__()
        self.head = head
    
    def add_node_head(self, node):
        if self.head is not None:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else: 
            self.head = node    

    def get_node(self, index):
        current = self.head
        while index>0:
            if current is None:
                return -1
            current = current.next
            index -= 1
        return current


    def add_node_tail(self, node):
        current = self.head
        if current is None:
            self.head = node

        while current.next:
            current = current.next
        
        current.next = node


    def insert(self, node, index):
        if index == 0:
            previous_head = self.head
            self.head = node
            self.head.next = previous_head
            return
        current = self.head
        previous = None
        while index > 0 and current is not None:
            index -=1
            previous = current
            current = current.next
        previous.next = node
        node.next = current


    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while index > 0 and current is not None:
            index -= 1
            previous = current
            current = current.next
        previous.next = current.next


    def oddEven(self):
        odds = None
        evens = None
        evensHead = None
        isOdd = True
        current = self.head
        while current is not None:
            if isOdd:
                if odds is not None:
                    odds.next = current
                    odds = current
                else:
                    odds = current
            else:
                if evens is not None:
                    evens.next = current
                    evens = current
                else:
                    evens = current
                    evensHead = evens
            current = current.next
            isOdd = not isOdd
        evens.next = None
        odds.next = evensHead


    def palindrome(self):
        current = mid = temp_head = self.head
        while current and current.next:
            current = current.next.next
            mid = mid.next
        node = None
        while mid:
            nxt = mid.next
            mid.next = node
            node = mid
            mid = nxt
        mid = node
        while mid:
            if mid.value != temp_head.value:
                return False
            mid = mid.next
            temp_head = temp_head.next
        return True       
        

    def reverse_iterative(self):
        current = self.head
        node = None
        while current:
            nxt = current.next
            current.next = node
            node = current
            current = nxt
        self.head = node
        

    def reverse_recursive(self):
        return self.__recursive_helper(self.head, None)


    def __recursive_helper(self, node, prev):
        if node:
            nxt = node.next
            node.next = prev
            prev = node
            return self.__recursive_helper(nxt, prev)
        else:
            self.head=prev
            return


    def __str__(self):
        current = self.head
        response = ""
        li = []
        while current is not None:
            li.append(str(current.value))
            # li.append("->")
            current = current.next
        return response.join(li)


n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
ll = LinkedList(n)

ll.insert(Node(6), 6)
ll.add_node_tail(Node(9))
ll.add_node_head(Node(8))
# print(ll.get_node(4).value)
print(ll)
ll.reverse_iterative()
print(ll)
ll.reverse_recursive()
print(ll)
# ll.oddEven()
# print(ll)
# ll.delete(1)
# print(ll)

n1 = Node(1, Node(2, Node(2, Node(2, Node(2, Node(1))))))
ll2 = LinkedList(n1)
print(ll2)
print(ll2.palindrome())

aa = "abcd"
print(aa[::-1])