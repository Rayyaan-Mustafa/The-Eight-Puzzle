import copy
import time

#default eight puzzle cases
trivial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
veryEasy = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
doable = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
oh_boy = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]

N_PUZZLE = 3 #dimensions of the puzzle. can change to accomadate different size puzzle boards

class Node:
    def __init__(self, puzzle):
        self.puzzle = puzzle # 2d array containg the puzzle
        self.heuristicCost = 0 # h(n)
        self.depth = 0 # g(n)
    
def main():

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
                user_puzzle[i][j] = int(input("Enter number (row {}, col {}): ".format(str(i+1), str(j+1))))
        print("The puzzle you entered is:")
        print_puzzle(user_puzzle)
        select_and_init_algorithm(user_puzzle)
    return

def init_default_puzzle_mode(): 
    """Returns puzzle selected by user."""
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
    """Prints the puzzle in a readable format."""
    for i in range(0, N_PUZZLE):
        print(puzzle[i])

def select_and_init_algorithm(puzzle):
    """Gets use input for heuristic choice and calls general_search function."""
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
    "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        general_search(puzzle, 1)
    if algorithm == "2":
        general_search(puzzle, 2)
    if algorithm == "3":
        general_search(puzzle, 3)

def general_search(problem, queueing_function):
    """General search function. Takes user heuristic choice and calls appropriate heuristic function in search function."""
    start_time = time.time()
    heuristic = Uniform_Heuristic
    if queueing_function == 1:
        heuristic = Uniform_Heuristic
    elif queueing_function == 2:
        heuristic = Misplaced_Tile_Heuristic
    elif queueing_function == 3:
        heuristic = Manhattan_Distance_Heuristic
    else:
        print("Invalid queueing function was selected. Defaulting to Uniform Cost Search.")

    expanded_nodes_count = 0
    max_queue_size = 0
    repeated_states = set()

    nodes = [] #queue to store nodes
    nodes.append(Node(problem)) #add initial state to queue

    while True:
        max_queue_size = max(max_queue_size, len(nodes))
        if len(nodes) == 0:
            return "failure"
        node = nodes.pop(0)
        if goal_test(node.puzzle, goal_state):
            print("Goal state! \n")
            print("Solution depth was: " + str(node.depth))
            print("Number of nodes expanded: " + str(expanded_nodes_count))
            print("Max queue size: " + str(max_queue_size))
            print()
            print("Time taken: " + str(time.time() - start_time))
            return node
            # return ["Goal state! \n", "Solution depth was: " + str(node.depth), "Number of nodes expanded: " + str(expanded_nodes_count), "Max queue size: " + str(max_queue_size), "Time taken: " + str(time.time() - start_time)]
        children = Expand(node, repeated_states)

        if expanded_nodes_count != 0:
            print("The best state to expand with a g(n) = " + str(node.depth) + " and h(n) = " + str(node.heuristicCost) + " is...")
            print_puzzle(node.puzzle)
        expanded_nodes_count += 1
        for i in range(len(children)):
            children[i].heuristicCost = heuristic(children[i].puzzle, goal_state, goal_state_positions) #sets heuristic cost of each child node
            nodes.append(children[i]) #adds children to queue
        #queueing function
        nodes = sorted(nodes, key=lambda n: (n.heuristicCost + n.depth, n.depth)) #sorts the queue by heuristic cost + depth
        

def goal_test(A, B):
    """Takes two puzzles as arguemnts and returns true if A and B are the same."""
    if A == B:
        return True
    else:
        return False

def Expand(node, repeated_states):
    """Takes node and set() of repeated_states as parameters and returns a list of all possible children of that node."""
    #finding the position of the '0' tile in the puzzle
    children = []
    row = 0
    col = 0
    found = False
    for i in range(N_PUZZLE):
        for j in range(N_PUZZLE):
            if node.puzzle[i][j] == 0:
                row = i
                col = j
                found = True
                break
        if found:
            break

    #only expands the node if it is possible (within bounds of the puzzle) AND if the node is not in repeated_states)
    #move the '0' tile left
    if col > 0:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row][col-1] = temp_puzzle[row][col-1], temp_puzzle[row][col]
        if (tuple(map(tuple, temp_puzzle))) not in repeated_states:
            repeated_states.add(tuple(map(tuple, temp_puzzle)))
            n = Node(temp_puzzle)
            n.depth = node.depth + 1
            children.append(n)
    #move the '0' tile right
    if col < N_PUZZLE - 1:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row][col+1] = temp_puzzle[row][col+1], temp_puzzle[row][col]
        if (tuple(map(tuple, temp_puzzle))) not in repeated_states:
            repeated_states.add(tuple(map(tuple, temp_puzzle)))
            n = Node(temp_puzzle)
            n.depth = node.depth + 1
            children.append(n)
    #move the '0' tile up 
    if row > 0:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row-1][col] = temp_puzzle[row-1][col], temp_puzzle[row][col]
        if (tuple(map(tuple, temp_puzzle))) not in repeated_states:
            repeated_states.add(tuple(map(tuple, temp_puzzle)))
            n = Node(temp_puzzle)
            n.depth = node.depth + 1
            children.append(n)
    #move the '0' tile down
    if row < N_PUZZLE - 1:
        temp_puzzle = copy.deepcopy(node.puzzle)
        temp_puzzle[row][col], temp_puzzle[row+1][col] = temp_puzzle[row+1][col], temp_puzzle[row][col]
        if (tuple(map(tuple, temp_puzzle))) not in repeated_states:
            repeated_states.add(tuple(map(tuple, temp_puzzle)))
            n = Node(temp_puzzle)
            n.depth = node.depth + 1
            children.append(n)
    return children

def Uniform_Heuristic(puzzle, goal_state, goal_state_positions):
    """Returns 0 for Uniform Cost Search."""
    return 0

def Manhattan_Distance_Heuristic(puzzle, goal_state, goal_state_positions):
    """Returns the sum of the Manhattan distances of each tile from the correct goal state position (excluding the '0' tile)."""
    count = 0
    for i in range(0, N_PUZZLE):
        for j in range(0, N_PUZZLE):  
            if (puzzle[i][j] != goal_state[i][j]) and puzzle[i][j] != 0:
                count += abs(goal_state_positions[puzzle[i][j]][0] - i) + abs(goal_state_positions[puzzle[i][j]][1] - j)
    return count     

def Misplaced_Tile_Heuristic(puzzle, goal_state, goal_state_positions):
    """Returns the number of misplaced tiles (excluding the '0' tile)."""
    count = 0
    for i in range(1, N_PUZZLE**2):
        if puzzle[goal_state_positions[i][0]][goal_state_positions[i][1]] != i:
            count += 1
    return count

def get_goal_state_positions(goal_state):
    """Returns a dictionary with information about the goal state. {key: tile number, value: (row, col)}"""
    goal_state_positions = dict()
    for i in range(0, N_PUZZLE):
        for j in range(0, N_PUZZLE):
            goal_state_positions[goal_state[i][j]] = (i, j)
    return goal_state_positions

def create_goal_state(N_PUZZLE):
    """Returns correct goal state puzzle of size N_PUZZLE x N_PUZZLE."""
    goal = [[0 for i in range(N_PUZZLE)] for j in range(N_PUZZLE)]
    count = 1
    for i in range(N_PUZZLE):
        for j in range(N_PUZZLE):
            goal[i][j] = count
            count += 1
    goal[-1][-1] = 0 #sets the last tile to '0'
    return goal

if __name__ == "__main__":
    goal_state = create_goal_state(N_PUZZLE) #creates goal state board based on N_PUZZLE dimensions
    goal_state_positions = get_goal_state_positions(goal_state) #creates dictionary of goal state positions

    ####testing (uncomment line 115, and comment out line 114 to test)

    # results = {}
    # depth0 = [[1,2,3],[4,5,6],[7,8,0]]
    # depth2 = [[1,2,3],[4,5,6],[0,7,8]]
    # depth4 = [[1,2,3],[5,0,6],[4,7,8]]
    # depth8 = [[1,3,6],[5,0,2],[4,7,8]]
    # depth12 = [[1,3,6],[5,0,7],[4,8,2]]
    # depth16 = [[1,6,7],[5,0,3],[4,8,2]]
    # depth20 = [[7,1,2],[4,8,5],[6,3,0]]
    # depth24 = [[0,7,2],[4,6,1],[3,5,8]]
    
    # results[0] = general_search(depth0,1)
    # results[2] = general_search(depth2,1)
    # results[4] = general_search(depth4,1)
    # results[8] = general_search(depth8,1)
    # results[12] = general_search(depth12,1)
    # results[16] = general_search(depth16,1)
    # results[20] = general_search(depth20,1)
    # results[24] = general_search(depth24,1)


    # for k,v in results.items():
    #     print("depth: {}".format(k))
    #     print(v)

    ####testing

    main()
