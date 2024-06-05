# Happy Number Algorithm

A happy number is a number that, when replaced by the sum of the squares of its digits repeatedly, eventually reaches the number 1. For example, 19 is a happy number because the process of summing the squares of its digits leads to 1.

The mathematical process of reaching convergence to 1 for a happy number involves iterating the sum of the squares of the digits until the number reaches 1.

## Solving for a happy number

To determine if a number is a happy number, we can use the fast and slow pointer technique:
- Initialize two variables, slow and fast, both set to the given number.
- Define a function next_num that takes a number and returns the sum of the squares of its digits.
- Move slow to next_num(slow).
- Move fast to next_num(next_num(fast)).
- If slow and fast ever become equal, return false (not a happy number).
- If fast ever becomes 1, return true (happy number).
