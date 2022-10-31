from collections import deque

#default eight puzzle cases
trivial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
veryEasy = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
doable = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
oh_boy = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]

N_PUZZLE = 3 #dimensions of the puzzle. can change to accomadate different size puzzle boards

def main():
    goal_state = create_goal_state(N_PUZZLE) #creates goal state board based on N_PUZZLE dimensions

    puzzle_mode = input("Welcome to Rayyaan's 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own. (Default puzzles are all 8 puzzles)" + '\n')
    #lets user select 1 of 4 default puzzles
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
    # if selected_difficulty == "5":
    #     print("Difficulty of 'Impossible' selected.")
    #     return impossible

def print_puzzle(puzzle):
    for i in range(0, N_PUZZLE):
        print(puzzle[i])

def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
    "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        uniform_cost_search(puzzle, 0)
    if algorithm == "2":
        uniform_cost_search(puzzle, 1)
    if algorithm == "3":
        uniform_cost_search(puzzle, 2)

def uniform_cost_search(puzzle, heuristic):
    starting_node = TreeNode.TreeNode(None, puzzle, 0, 0)
    working_queue = []
    repeated_states = dict()
    min_heap_esque_queue.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states[starting_node.board_to_tuple()] = "This is the parent board"
    stack_to_print = [] # the board states are stored in a stack
    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        # the node from the queue being considered/checked
        node_from_queue = min_heap_esque_queue.heappop(working_queue)
        repeated_states[node_from_queue.board_to_tuple()] = "This can be anything"
        if node_from_queue.solved(): # check if the current state of the board is the solution
            while len(stack_to_print) > 0: # the stack of nodes for the traceback
                print_puzzle(stack_to_print.pop())
            print("Number of nodes expanded:", num_nodes_expanded)
            print("Max queue size:", max_queue_size)
            return node_from_queue
        stack_to_print.append(node_from_queue.board)

def goal_test(A, B):
    if A == B:
        return True
    else:
        return False

def general_search(problem, queueing_function):
    if queueing_function == 1:
        pass
    elif queueing_function == 2:
        pass
    elif queueing_function == 3:
        pass


    nodes = deque()
    #add initial state to deque
    nodes.append(initial_state)

    while True:
        if len(nodes) == 0:
            return "failure"
        node = nodes.popleft()
        if goal_test(node, goal_state):
            return node
        nodes = queueing_function(nodes, expand(node, problem.operators))



def expand(node, ):
    pass


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
    main()

