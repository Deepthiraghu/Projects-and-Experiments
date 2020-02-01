
## Formulation of the search problem:
We are using best first approach where from state of the board the heuristic function will choose the best possible next state of the board to reach the goal state.

## State space: 
All possible arrangement of 15 numbered tiles and an empty tile (0) on a 4x4 board

## Initial state: 
Given input board

## Successor function:
s' -> SUCC(s)
s is the current state (arrangement) of the board
s' is the next state (arrangement) of the board, guided/defined by the permitted moves based on the variant

## Edge weights (cost):
There is no involved cost in this problem. Every move is assumed to have the same cost.

## Goal state:
The board:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 0

## Heuristic function:
h(s) = g(s) + f(s) where,
g(s) = hops taken so far 
f(s) = manhattan distance from successor state to the goal state
We go to the successor state which has minimum h(s)

## Why this is admissible:
The optimal solution h*(s) involves each of the misplaced tile to be moved a maximum of the number of hops to reach the goal state. Our heuristic function h(s) will always give an estimate that is less than this. Hence, our heuristic function is admissible [ie 0 <= h(s) < h*(s)]

## How the search algorithm works:
The search algorithm takes the initial board and adds it to the fringe. For each of the next successor states of the board, it picks the best possible successor based on the heuristic function - minimum ((hops taken so far) + (manhattan distance from successor state to the goal state)) and adds it to the optimal solution. To determine if the given board is solvable or not, we used permutation inversion parity check.

## Problems faced:
The given solution took a very long time to reach goal state. After applying A* search, the solution was reached faster. 
If initial state is the goal state, the given solution did not cover this case. 
Initially, we could not determine if a board is solvable or not. Then we applied permutation inversion to check this.
For certain hard boards, the code runs too long since it executes indefinitely. This problem still exists, and can be overcome by applying iterative deepening search - IDA* (implementation not completed)

## Other heuristic function tried by the team and the reason of failure:
We tried to use the number of misplaced tiles as a heuristic function. But later, we found that manhattan distance between successor state to goal state worked as a better heuristic.

