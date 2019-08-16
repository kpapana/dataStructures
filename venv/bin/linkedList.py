"""
Linked list implementation in python.

is_empty() - return true if the list is empty, else false
print_list() - print the entire contents of list
append() - to add nodes to the end of linked list
prepend() - to add nodes to the beginning of linked list
insert_after_node() - to add a node after a specific node
search_list() - returns the node matching with search data
delete() - deletes the last node in the list
delete_node() - deletes node that data matching with input

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        return False

    def print_list(self):
        next_node=self.head
        while next_node:
            print(next_node.data)
            next_node=next_node.next

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail=new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.append(data)
            return
        new_node.next = self.head

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in list")
            return
        # check if prev_node is tail, if yes, then perform append. At this point insert after node is same as append
        if prev_node.next is None:
            self.append(data)
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search_list(self,data):
        last_node=self.head
        while last_node.next:
            if last_node.data == data:
                return last_node
            last_node = last_node.next
        return last_node

    def delete(self):
        if self.is_empty():
            print("Nothing to delete, list empty")
            return False
        current_node=self.head
        prev_node=self.head
        while current_node.next:
            prev_node=current_node
            current_node=current_node.next
        prev_node.next=None
        self.tail=prev_node
        return True

    def delete_node(self, data):
        if self.is_empty():
            print("Nothing to delete, list empty")
            return False

        if self.head == self.tail:
            if self.head.data == data:
                self.head=None
            else:
                print("Search data element does not exist in list")
                return

        if self.head.data == data:
            self.head = self.head.next
            return True
        cur_node = self.head.next
        prev_node = self.head
        while prev_node.next:
            if cur_node.data == data:
                prev_node.next=cur_node.next
                return True
            prev_node=cur_node
            cur_node=cur_node.next
        print("Nothing to delete, data not found in list")
        return
