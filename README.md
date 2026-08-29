# AI-Practice

## Question 01 -- 8-Puzzle using DFS

### Aim
To implement DFS for 8-Puzzle problem, find the goal state, and return the actual solution path from the initial state

### Approach 

1. First, we generate valid neighbouring states from the given states using the possible moves.
2. We implement DFS to explore the generated states and search for the goal state.
3. We used stack data structure to perform the DFS traversal.
4. A parent dictionary is maintained to keep track of how each state was reached.
5. When the goal state is found, the parent dictionary used to reconstruct the actual solution path.


### Source Code:
The implementation is available in:
'01_8_Puzzle_DFS/8_puzzles_dfs.py'

### Conclusion

This program successfully demonstrates the use of DFS on the transition model.
Furthermore, the program avoids redundant states and finds the goal state, allowing the 8-Puzzle solution to execute seamlesly.


## Question 02 -- Water Jug Problem Using BFS

### Aim
To implement the Water Jug Problem using Breadth First Search (BFS) and find a valid path from the initial state to the given goal state.

### Approach / Algorithm

1. Represent the amount of water in Jug A and Jug B as a state(A,B).
2. Generates Valid neighbours from the current state using the possible operations:
      1. Fill Jug A
      2. Fill Jug B
      3. Empty Jug A
      4. Empty Jug B
      5. Pour water from Jug A to Jug B
      6. Pour water from Jug B to Jug A
3. while generating neighbour, evaluate the current amount of water and remaining capacity of the destination jug to perform valid pour operation.
4. Use a queue to implement BFS and explore the states level by level.
5. Use a visited set to avoid processing redundant states.
6. use a parent dictionary to store the relationship between e newly discovered state and its current state.
7. compare each state with the given goal state.
8. When the goal is found, trace the states back using the parent dictionary and reverse the path to obtain actual sequence of states.
9. if the queue becomes empty before reaching the goal, return None, which indicates the goal not found.

### Source Code
The implementation is available in:
'02_Water_Jug_Problem/water_jug_bfs.py'

### Conclusion:

This program successfully demonstrates the use of BFS for solving the Water Jug Problem. Furthermore, it generates valid neighbours for each state, avoids redundant states using a visited set, and uses a parent dictionary to reconstruct the actual path.
