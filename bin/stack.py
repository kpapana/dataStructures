"""
performs regular stack operations using list

push() - to add items to stack
pop() - to delete item on the top
is_empty() - to check if stack is empty
peek() - to see the item on the top
get_stack() - to return all items on stack

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items

