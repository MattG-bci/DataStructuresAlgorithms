from unittest.mock import NonCallableMagicMock


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, val):
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while True:
            if itr.next is None:
                itr.next = Node(data, None)
                return
            itr = itr.next

    def display(self):
        if self.head is None:
            raise "Linked list is empty"

        itr = self.head
        while itr:
            print(itr.val)
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    
    def remove(self, idx):
        if idx==0:
            self.head = self.head.next
            return
        
        position = 0
        iter = self.head
        while iter:
            if position == idx - 1:
                iter.next = iter.next.next
                return

            iter = iter.next
            position += 1
    
    def insert_at(self, idx, data):
        if idx == 0:
            self.insert_at_begining(data)
        
        if idx == self.get_length():
            self.insert_at_end(data)

        position = 0
        iter = self.head
        while iter:
            if position == idx - 1:
                iter.next = Node(data, iter.next)
                return
            position += 1
            iter = iter.next

    # Functions as additional exercises.

    def remove_by_value(self, data):
        if data == self.head.val:
            self.head = self.head.next
            return

        iter = self.head
        while iter:
            if iter.next.val == data:
                iter.next = iter.next.next
                return
            iter = iter.next

    def insert_after_value(self, data_after, data_to_insert):
        iter = self.head
        while iter:
            if iter.val == data_after:
                iter.next = Node(data_to_insert, iter.next)
                return
            iter = iter.next



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(7)
    ll.insert_at_begining(5)
    ll.insert_at_begining(3)
    ll.insert_at_begining(9)
    ll.insert_at_end(14)
    ll.insert_values([7, 6, 3, 3]) # removes previously entered values.
    ll.display()
    print(f"The length of the linked list: {ll.get_length()}")
    ll.remove(1)
    ll.insert_at(1, 8)
    ll.display()
    print("=========Solution#1=========")
    ll.remove_by_value(7)
    ll.display()
    print("=========Solution#2=========")
    ll.insert_after_value(8, 4)
    ll.display()

