#!/usr/bin/env python3
""" Singly linked lists """


class Node:
    """ Defines the Node class"""

    def __init__(self, data):
        """ Initializes the Node class with a node: `data` part and a
        reference to the next element
        """
        self.data = data
        self.next = None


class LinkedList:
    """ LinkedList class definition """

    def __init__(self):
        """ Initializes the LinkedList class with a pointer to the head
        element
        """
        self.head = None

    def print_list(self):
        """ Prints out the contents of the linked list """
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        """ Inserts a new node to the end of the linked list """
        new_node = Node(data)

        # Check for an empty linked list
        if self.head is None:
            self.head = new_node
            return

        # Append new_node to end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """ Adds a new node to the beginning of the list """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """ Inserts a new node after the specified prev_node """
        if not prev_node:
            print('Previous node does not exist')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """ Deletes a node based on the value of the data """
        # Case if node is head:
        curr_node = self.head
        if curr_node and curr_node.data = key:
            self.head = curr_node.next
            curr_node = None
            return
        # If node is not head
        # We need to keep track of the previous node
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        # Handle case where the node doesn't exist
        if curr_node is None:
            return

        # Delete curr_node
        prev.next = curr_node.next
        curr_node = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("E")

# Prepend a node
llist.prepend("D")

# Insert a node at a specific position
llist.insert_after_node(llist.head.next, "A")

# Delete a node
llist.delete_node("B")
llist.delete_node("E")

llist.print_list()
