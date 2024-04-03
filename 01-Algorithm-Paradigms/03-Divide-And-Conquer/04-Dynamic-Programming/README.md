# Dynamic Programming

Is a method used to solve complex problems by breaking them down into simpler subproblems. It involves solving these subproblems independently and then combining their solutions to find the optimal solution to the original problem. 

Dynamic programming can be implemented using two main approaches:
- **Top-Down Approach (Memoization)**: This approach starts with the final solution and recursively breaks it down into smaller subproblems. The results of solved subproblems are stored in a table to avoid redundant calculations.
- **Bottom-Up Approach (Tabulation)**: In this approach, the smallest subproblems are solved first, gradually building up to the final solution by storing the results of solved subproblems in a table.

By storing the results of subproblems, dynamic programming avoids redundant calculations and optimizes the overall solution process.

## Advantages
- Being a recursive programming technique, it reduces the lines of code.
- It speeds up the processing, as we use the answer of a
  previously-calculated subproblem to get the next one.

# Disadvantages
- It takes a lot of memory to store the calculated result of every subproblem without ensuring if the stored value will be utilized or not, which leads to unnecessary memory utilization.
- There is no general form for problems solved by dynamic programming, i.e., every problem has to be solved in its own way.
