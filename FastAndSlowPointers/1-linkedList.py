#!/usr/bin/env python3
""" A linked List """


class ListNode:
    def __init__(self, value=0, next=None):
        """ Initialize a linked list node """
        self.value = value
        self.next = next


def create_linked_list_with_cycle():
    """ Creates a linkedlist with a cycle """
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2          # Create a cycle

    return node1


def has_cycle(head):
    """ Checks if a linkedlist has a cycle """
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


head = create_linked_list_with_cycle()
print(has_cycle(head))
