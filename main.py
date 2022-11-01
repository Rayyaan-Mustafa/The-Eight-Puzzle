from collections import deque
import copy

#default eight puzzle cases
trivial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
veryEasy = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
doable = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
oh_boy = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]

N_PUZZLE = 3 #dimensions of the puzzle. can change to accomadate different size puzzle boards

class Node:
    def __init(self, puzzle):
        self.puzzle = puzzle #2d array containg the puzzle
        self.heuristicCost = 0 
        self.depth = 0
 

def main():
    goal_state = create_goal_state(N_PUZZLE) #creates goal state board based on N_PUZZLE dimensions
    goal_state_positions = get_goal_state_positions(goal_state) #creates dictionary of goal state positions

    puzzle_mode = input("Welcome to Rayyaan's 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own. (Default puzzles are all 8 puzzles)" + '\n')
    #lets user select 1 of 5 default puzzles
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode()) 
    #lets user create their own puzzle
    elif puzzle_mode == "2":
        print("Enter numbers left to right, top to bottom. Hit ENTER after every number.")
        user_puzzle = [[0 for i in range(N_PUZZLE)] for j in range(N_PUZZLE)]
        for i in range(N_PUZZLE):
            for j in range(N_PUZZLE):
                user_puzzle[i][j] = input("Enter number (row {}, col {}): ".format(str(i+1), str(j+1)))
        print("The puzzle you entered is:")
        print_puzzle(user_puzzle)
        select_and_init_algorithm(user_puzzle)
    return

def init_default_puzzle_mode(): 
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 4." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        print("The puzzle is:")
        print_puzzle(trivial)
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        print("The puzzle is:")
        print_puzzle(veryEasy)
        return veryEasy
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        print("The puzzle is:")
        print_puzzle(easy)
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Doable' selected.")
        print("The puzzle is:")
        print_puzzle(doable)
        return doable
    if selected_difficulty == "4":
        print("Difficulty of 'Oh Boy' selected.")
        print("The puzzle is:")
        print_puzzle(oh_boy)
        return oh_boy

def print_puzzle(puzzle):
    for i in range(0, N_PUZZLE):
        print(puzzle[i])

def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
    "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        general_search(puzzle, 0)
    if algorithm == "2":
        general_search(puzzle, 1)
    if algorithm == "3":
        general_search(puzzle, 2)

def general_search(problem, queueing_function):
    if queueing_function == 1:
        pass
    elif queueing_function == 2:
        pass
    elif queueing_function == 3:
        pass

    expanded_nodes_count = -1
    max_queue_size = 0
    repeated_states = set()

    nodes = deque()
    #add initial state to deque
    nodes.append(Node(problem))

    while True:
        if len(nodes) == 0:
            return "failure"
        node = nodes.popleft()
        if goal_test(node, goal_state):
            print("Goal state! \n")
            print("Solution depth was: " + str(node.depth))
            print("Number of nodes expanded: " + str(expanded_nodes_count))
            print("Max queue size: " + str(max_queue_size))
            return node
        nodes = queueing_function(nodes, Expand(node))

def goal_test(A, B):
    if A == B:
        return True
    else:
        return False

def Expand(node, repeated_states):
    #finding the position of the '0' tile in the puzzle
    children = []
    row = col = 0
    for i in range(N_PUZZLE):
        for j in range(N_PUZZLE):
            if node.puzzle[i][j] == 0:
                row = i
                col= j
                break
    #move the '0' tile left
    if col > 0:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row][col-1] = temp_puzzle[row][col-1], temp_puzzle[row][col]
        n = Node(temp_puzzle)
        children.append(n)
    #move the '0' tile right
    if col < N_PUZZLE - 1:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row][col+1] = temp_puzzle[row][col+1], temp_puzzle[row][col]
        n = Node(temp_puzzle)
        children.append(n)
    #move the '0' tile up 
    if row > 0:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row-1][col] = temp_puzzle[row-1][col], temp_puzzle[row][col]
        n = Node(temp_puzzle)
        children.append(n)
    #move the '0' tile down
    if row < N_PUZZLE - 1:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row+1][col] = temp_puzzle[row+1][col], temp_puzzle[row][col]
        n = Node(temp_puzzle)
        children.append(n)
    return children

    
    

def Manhattan_Distance_Heuristic(puzzle, goal_state, goal_state_positions):
    count = 0
    for i in range(0, N_PUZZLE):
        for j in range(0, N_PUZZLE):  
            if (puzzle[i][j] != goal_state[i][j]) and puzzle[i][j] != 0:
                count += abs(goal_state_positions[puzzle[i][j]][0] - i) + abs(goal_state_positions[puzzle[i][j]][1] - j)
    return count     

def Misplaced_Tile_Heuristic(puzzle, goal_state, goal_state_positions):
    count = 0
    for i in range(1, N_PUZZLE**2):
        if puzzle[goal_state_positions[i][0]][goal_state_positions[i][1]] != i:
            count += 1
    return count

def get_goal_state_positions(goal_state):
    goal_state_positions = dict()
    for i in range(0, N_PUZZLE):
        for j in range(0, N_PUZZLE):
            goal_state_positions[goal_state[i][j]] = (i, j)
    return goal_state_positions

def create_goal_state(N_PUZZLE):
    goal = [[0 for i in range(N_PUZZLE)] for j in range(N_PUZZLE)]
    count = 1
    for i in range(N_PUZZLE):
        for j in range(N_PUZZLE):
            goal[i][j] = count
            count += 1
    goal[-1][-1] = 0
    return goal


if __name__ == "__main__":
    # main()
