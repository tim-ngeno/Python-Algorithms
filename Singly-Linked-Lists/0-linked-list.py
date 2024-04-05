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
        """ Adds a new node to the beginning og the list """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.prepend("D")

llist.append("E")

llist.print_list()
