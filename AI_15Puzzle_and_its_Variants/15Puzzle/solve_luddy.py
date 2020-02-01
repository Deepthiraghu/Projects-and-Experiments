#!/usr/local/bin/python3
# solve_luddy.py : Sliding tile puzzle solver
#
# Code by: [Deepthi Raghu (draghu), Sudharshan (ssowmiya), Naveen (naviri)]
#
# Based on skeleton code by D. Crandall, September 2019
#
from queue import PriorityQueue
import sys

MOVES = {"R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1, 0)}
MOVES_CIRCULAR = {"R": (0, -3), "L": (0, 3), "D": (-3, 0), "U": (3, 0)}
MOVES_LUDDY = {"A": (2, 1), "B": (2, -1), "C": (-2, 1), "D": (-2, -1), "E": (1, 2), "F": (1, -2), "G": (-1, 2), "H": (-1, -2)} 

def rowcol2ind(row, col):
    return row*4 + col

def ind2rowcol(ind):
    return (int(ind/4), ind % 4)

def valid_index(row, col):
    return 0 <= row <= 3 and 0 <= col <= 3

def swap_ind(list, ind1, ind2):
    return list[0:ind1] + (list[ind2],) + list[ind1+1:ind2] + (list[ind1],) + list[ind2+1:]

def swap_tiles(state, row1, col1, row2, col2):
    return swap_ind(state, *(sorted((rowcol2ind(row1, col1), rowcol2ind(row2, col2)))))

def printable_board(row):
    return ['%3d %3d %3d %3d' % (row[j:(j+4)]) for j in range(0, 16, 4)]

# return a list of possible successor states
def successors(state, variant):
    (empty_row, empty_col) = ind2rowcol(state.index(0))
    # for original variant, consider moves from MOVES dictionary
    if variant == "original":
        return [(swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c) for (c, (i, j)) in MOVES.items() if valid_index(empty_row+i, empty_col+j)]
    # for circular variant, consider moves from MOVES dictionary and MOVES_CIRCULAR directory
    elif variant == "circular":
        succ_arr = []
        for (c, (i, j)) in MOVES_CIRCULAR.items():
             if valid_index(empty_row+i, empty_col+j):
                succ_arr.append((swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c))
        for (c, (i, j)) in MOVES.items():
             if valid_index(empty_row+i, empty_col+j):
                succ_arr.append((swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c))
        return succ_arr
    # for luddy variant, take moves from MOVES_LUDDY dictionary
    if variant == "luddy":
        return [(swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c) for (c, (i, j)) in MOVES_LUDDY.items() if valid_index(empty_row+i, empty_col+j)]

# function to calculate manhattan distance between given state and goal state
def calculateManhattanDistance(succ):
    manhattanDistance = 0
    for i in range(len(succ)):
        element = succ[i]
        currentIndex = ind2rowcol(i)
        goalIndex = ind2rowcol(element-1)
        manhattanDistance += sum([abs(goalIndex[i]-currentIndex[i])
                                  for i in range(len(goalIndex))])
    return manhattanDistance

# function to calculate number of misplaced tiles
# heuristic initially experimented with, but not considered in the final heuristic function
def calculateMisplacedTilesCount(succ):
    misplacedTilesCount = 0
    for i in range(len(succ)):
        if i != succ[i]-1:
            misplacedTilesCount = misplacedTilesCount+1
    return misplacedTilesCount

# check if we've reached the goal
def is_goal(state):
    return sorted(state[:-1]) == list(state[:-1]) and state[-1] == 0

# Permutation inversion to check if board is solvable
def permutationInversionCheck(board):
    permutationInversionCount = 0
    # for each element, count the number of elements that occurs after it and has lesser value
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if(board[i] > board[j] and board[j]!=0):
                permutationInversionCount = permutationInversionCount+1
    row, col = ind2rowcol(board.index(0))
    # add the row number of empty tile to the above count and calculate count%2 to find parity
    permutationInversionCount = permutationInversionCount + row+1
    if permutationInversionCount % 2 == 0:
        return True
    else:
        return False

# The solver! - using A* search with heuristic as minimum of ((hops taken so far) + (manhattan distance from successor state to the goal state))
def solve(initial_board, variant):
    # check for permutation inversion parity 
    if not permutationInversionCheck(initial_board):
        return ("Inf")
    fringe = PriorityQueue()
    # put initial board to fringe
    fringe.put((0, initial_board, ""))
    jumpCount = 0
    visitedState = []
    while not fringe.empty():
        # get state from fringe based on priority - minimum value of (hops taken so far) + (manhattan distance from successor state to the goal state)
        (_, state, route_so_far) = fringe.get()
        # add state to visited
        visitedState.append(state)
        # if the start state is the goal state, return empty route
        if is_goal(state):
            return(route_so_far)
        jumpCount = jumpCount+1
        # loop through possible next successor states
        for (succ, move) in successors(state, variant):
            # if the successor state is the goal state, return route
            if is_goal(succ):
                return(route_so_far + move)
            # calculate heuristic function (hops taken so far) + (manhattan distance from successor state to the goal state)
            # and add state to fringe
            if (succ not in visitedState):
                fringe.put((calculateManhattanDistance(succ) +
                            jumpCount, succ, route_so_far + move))
    return False

# test cases
if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise(Exception("Error: expected 2 arguments"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [int(i) for i in line.split()]

    if len(start_state) != 16:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" + "\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state), sys.argv[2])

    print("Solution found in " + str(len(route)) + " moves:" + "\n" + route)