#!/usr/bin/env python3
""" Stack Data Structure """


class Stack():
    """
    A Stack Data Structure class to implement a Stack and its operations
    """

    def __init__(self):
        """
        Initializes the stack data structure with an empty list
        """
        self.items = []

    def push(self, item):
        """
        Inserts a new item to the end of the stack
        """
        self.items.append(item)

    def pop(self):
        """
        Removes an item from the end of the list and returns it
        """
        return self.items.pop()

    def is_empty(self):
        """
        Checks if the list of items is empty and returns a boolean value
        """
        return self.items == []

    def peek(self):
        """
        Returns the top element from the stack
        """
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        """
        Returns a list containing all the elements
        """
        return self.items


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push('A')
    my_stack.push('B')

    print(my_stack.get_stack())

    my_stack.push('C')
    print(my_stack.get_stack())

    my_stack.pop()
    print(my_stack.get_stack())

    stack_items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for i in stack_items:
        my_stack.push(i)

        print(my_stack.get_stack())

        print(my_stack.peek())
