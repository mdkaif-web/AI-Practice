# AI-Practice
## Question 01 -- 8-Puzzle using DFS

## Aim
To implement DFS for 8-Puzzle problem, find the goal state, and return the actual solution path from the initial state

### Approach 

1. First, we generate valid neighbouring states from the given states using the possible moves.
2. We implement DFS to explore the generated states and search for the goal state.
3. We used stack data structure to perform the DFS traversal.
4. A parent dictionary is maintained to keep track of how each state was reached.
5. When the goal state is found, the parent dictionary used to reconstruct the actual solution path.


## Source Code:
The implementation is available in:
'01_8_Puzzle_DFS/8_puzzles_dfs.py'

### Conclusion

This program successfully demonstrates the use of DFS on the transition model.
Furthermore, the program avoids redundant states and finds the goal state, allowing the 8-Puzzle solution to execute seamlesly.
