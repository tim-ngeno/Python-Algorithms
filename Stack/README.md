# Stack Data Structure in Python

## Introduction
A stack is a fundamental data structure that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. Stacks are widely used in computer science for their simplicity and efficiency. They find applications in various scenarios ranging from function call management to parsing expressions.

## Stack Operations
### Push
When we push an element onto a stack, it's like adding a book to a stack of books. The newly added book becomes the top of the stack, just like the last book placed on top of the pile. Thus, pushing elements onto a stack involves inserting them onto the top, with the latest element becoming the new top.

### Pop
Pop:
Popping from a stack is similar to taking the top book off the stack and putting it aside. This action follows the principle of Last-In, First-Out (LIFO), where the most recently added element (the top one) is the first to be removed. So, when we pop an element from the stack, we are effectively removing the top element.

### Peek
Another thing that we can do is view the top element of the stack so we can ask the data structure: “What’s the top element?” and it can give that to us using the peek operation. Note that the peek operation does not remove the top element, it merely returns it. This operation allows us to inspect the top element without altering the stack's structure.


## Python Implementation
In Python, we can easily implement a stack using a list. Here's a simple implementation:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
```

In this implementation, `push()` adds an item to the top of the stack, `pop()` removes and returns the top item, `top()` returns the top item without removing it, and `is_empty()` checks if the stack is empty.

## Applications
### 1. Managing Function Calls
Stacks are extensively used in programming languages to manage function calls. When a function is called, its execution context (including local variables and return address) is pushed onto the stack. When the function returns, its context is popped from the stack, allowing the program to return to the caller.

### 2. Parsing Expressions
Stacks are helpful in parsing expressions, especially infix to postfix or prefix conversions. Operators and operands can be pushed onto the stack, and operations can be performed based on their precedence and associativity.

### 3. Undo/Redo Functionality
In applications where undo and redo functionalities are required, stacks can be used to store the states of the system. Each action performed by the user can be pushed onto the stack, allowing for easy undoing by popping from the stack.

## Problems and Solutions
### Problem: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
```python
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
```

## Additional Resources
- [Python documentation on stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)
- [GeeksforGeeks article on stacks in Python](https://www.geeksforgeeks.org/stack-in-python/)
- [Stacks and Queues on Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
