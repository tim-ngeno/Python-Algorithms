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

    def find_len(self):
        """ Calculates the length of a linked list iteratively """
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def find_len_recursive(self, node):
        """ Calculates the length of a linked list recursively """
        if node is None:
            return 0
        return 1 + self.find_len_recursive(node.next)

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
        if curr_node and curr_node.data == key:
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

    def delete_node_at_pos(self, pos):
        """ Deletes a node at a specified position """
        if self.head:
            curr_node = self.head
            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return

            prev = None
            count = 0
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1

            if curr_node is None:
                return

    def swap_nodes(self, key1, key2):
        """ Swaps two nodes' positions in the linked list """
        if key1 == key2:
            return

        prev = None
        curr = self.head
        while curr and curr.data != key1:
            prev = curr
            curr = curr.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr or not curr_2:
            return

        if prev:
            prev.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr
        else:
            self.head = curr

        curr.next, curr_2.next = curr_2.next, curr.next

    def reverse(self):
        """ Reverses the order of a linked list """
        def _reverse_recursive(curr, prev):
            """ Helper function to reverse the linked list """
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)
        self.head = _reverse_recursive(curr=self.head, prev=None)

    def merge_sorted(self, llist):
        """ Merges two linked lists and returns a sorted linked list """
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q

        if not q:
            s.next = p

        self.head = new_head
        return self.head


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
print(f'The length of the linked list: {llist.find_len()}')

llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

# Prepend a node
llist.prepend("D")

# Insert a node at a specific position
llist.insert_after_node(llist.head.next, "A")


# Reverse a linked list
print("Current linked list:")
llist.print_list()
print("Reversed list: ")
llist.reverse()

# Delete a node
llist.delete_node("B")
llist.delete_node("E")

# Delete a node at specified position
llist.delete_node_at_pos(0)

llist.print_list()
print(f'The length of the linked list: {llist.find_len()}')


# Test sorting

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()
