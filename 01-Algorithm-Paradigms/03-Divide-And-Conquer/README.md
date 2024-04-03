# Divide and Conquer

The Divide and Conquer paradigm is a problem-solving approach that involves breaking down a problem into smaller, more manageable subproblems. This process continues recursively until the subproblems become simple enough to solve directly. The key steps in the Divide and Conquer strategy are:

### Divide
- The initial problem is divided into smaller subproblems that are similar to the original problem but simpler in nature.

### Conquer
- Each subproblem is solved independently. This step typically involves recursively applying the same Divide and Conquer approach to the subproblems.

### Combine
- The solutions to the subproblems are then combined to form a solution to the original problem.

By breaking down complex problems into smaller, more manageable parts, Divide and Conquer algorithms can often lead to efficient solutions. This approach is commonly used in algorithms like merge sort, quicksort, and binary search, where dividing the problem simplifies the overall solution process.


## Advantages
- It can be optimal for a general case solution where the problem is easy to divide, and the subproblem at some level is easy to solve.
- It makes efficient use of memory cache because, when the problem gets divided into subproblems, it becomes smaller enough to be easily solved in the cache itself.


## Disadvantages
- It uses recursive approach, which can ne more complicated in cases of a big dataset
- Since the problem is solved using recursion, it may end up duplicating some subproblems and lead to huge recursive stacks, which consequently consumes extra space.
