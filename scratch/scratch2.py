class Node(object):
    def __init__(self, value:int, next:object=None):
        super().__init__()
        self.value = value
        self.next = next
    
class LinkedList(object):
    def __init__(self, node=None):
        self.head = node

    def __str__(self):
        curr = self.head
        # print(id(curr))
        li=[]
        while curr:
            # print(curr.value, end="")
            li.append(str(curr.value))
            curr = curr.next
        return "".join(li)

    def reverse_iterartive(self):
        curr = self.head
        prev = None
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        self.head = prev

    def reverse_recursive(self):
        return self.__reverse_helper(None, self.head)
        

    def __reverse_helper(self, previous, current):
        if not current:
            self.head = previous
            return

        _next = current.next
        current.next = previous
        previous = current
        return self.__reverse_helper(previous, _next)

    def remove_item(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return True
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def remove_item_recursive(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return 
        return self.__remove_item_helper(value, self.head.next, self.head)

    def __remove_item_helper(self, value, current, previous):
        if current and current.value==value:
            previous.next = current.next
            return
        return self.__remove_item_helper(value, current.next, current)
        
    def odd_even(self):
        odd = True
        odd_head = None
        odd_tail = None
        even_head = None
        even_tail = None
        current = self.head
        while current:
            if odd:
                if not odd_head:
                    odd_head = odd_tail = current
                else:
                    odd_tail.next = current
                    odd_tail = current
            else:
                if not even_head:
                    even_head = even_tail= current
                else:
                    even_tail.next = current
                    even_tail = current
            odd = not odd
            current = current.next
        odd_tail.next = even_head
        even_tail.next = None

    def odd_even_recursive(self):
        return self.__oe_helper(self.head, True, None, None, None)

    def __oe_helper(self, current, isOdd, odd, even, even_head):
        if current:
            if isOdd:
                if not odd:
                    odd = current
                else:
                    odd.next = current
                    odd = current
            else:
                if not even:
                    even = even_head = current
                else:
                    even.next = current
                    even = current
            return self.__oe_helper(current.next, not isOdd, odd, even, even_head)
        odd.next = even_head


        


def main():
    n1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    ll = LinkedList(n1)
    # print(ll)
    # ll.reverse_iterartive()
    # print(n1.next.value)
    # ll.reverse_recursive()
    # print(ll)
    # ll.remove_item(5)
    # print(ll)
    # ll.remove_item_recursive(5)
    # print(ll)
    # ll.reverse_recursive()
    print(ll)
    # ll.odd_even()
    ll.odd_even_recursive()
    print(ll)


if __name__ == "__main__":
    main()


