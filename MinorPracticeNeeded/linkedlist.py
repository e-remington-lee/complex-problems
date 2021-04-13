class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        super().__init__()
        self.head = head


    def test(self):
        current = self.head
        current = 5
        print(self.head)

    
    def add_node(self, node):
        if self.head is not None:
            self.head.next = node
            self.head = node
        else: 
            self.head = node


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

    def odd_even(self):
        index = 1
        odd_head = None
        odd_tail = None
        even_head = None
        even_tail = None
        current = self.head
        while current is not None:
            if index % 2 == 1:
                if odd_head is not None:
                    odd_head.next = current
                    odd_head = current
                else:
                    odd_head = current

                if odd_tail is None:
                    odd_tail = current
                elif odd_tail.next is None:
                    odd_head.next = current
            else:
                if even_head is not None:
                    even_head.next = current
                    even_head = current
                else:
                    even_head = current

                if even_tail is None:
                    even_tail = current
                elif even_tail.next is None:
                    even_head.next = current
            index +=1
            current = current.next
        odd_head.next = even_tail
        while odd_tail is not None:
            print(odd_tail.value)
            odd_tail = odd_tail.next
        

    def reverse_iterative(self):
        current = self.head
        response = ""
        li = []
        while current is not None:
            li.insert(0, str(current.value))
            current = current.next
        return response.join(li)


    def reverse_recursive(self):
        return self.__recursive_helper(self.head, [])


    def __recursive_helper(self, node, li):
        if node is not None:
            li.insert(0, str(node.value))
            return self.__recursive_helper(node.next, li)
        else:
            return "".join(li)


    def __str__(self):
        current = self.head
        response = ""
        li = []
        while current is not None:
            li.append(str(current.value))
            current = current.next
        return response.join(li)


# n = Node(5, Node(4, Node(3)))
n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
ll = LinkedList(n)
print(ll.test())
print(ll)
ll.insert(Node(6), 8)
print("Doesn't work with odd length of ll, infinite loop if so")
print(ll)
ll.odd_even()
print(ll)
ll.delete(1)
print(ll)





