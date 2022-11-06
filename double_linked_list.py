class Node:
    def __init__(self, val=None, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
    

    def insert_at_beginning(self, val):
        if self.head == None:
            node = Node(val, None, self.head)
            self.head = node
        else:
            node = Node(val, None, self.head)
            self.head.prev = node
            self.head = node


    def print_forward(self):
        iter = self.head
        while iter:
            print(iter.val)
            iter = iter.next


    def print_backward(self):
        iter = self.head
        while iter.next:
            iter = iter.next

        while iter:
            print(iter.val)
            iter = iter.prev


if __name__ == "__main__":
    dls = DoubleLinkedList()
    dls.insert_at_beginning(5)
    dls.insert_at_beginning(7)
    dls.insert_at_beginning(3)
    #dls.print_forward()
    dls.print_backward()

