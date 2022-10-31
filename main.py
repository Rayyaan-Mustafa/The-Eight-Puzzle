from collections import deque

def main():
    N_PUZZLE = 3 #dimensions of the puzzle. can change to accomadate different size puzzle boards
    goal_state = create_goal_state(N_PUZZLE)
    loop = True

    while loop:
        initial_state = [[0 for i in range(N_PUZZLE)] for j in range(N_PUZZLE)]
        print("Eight Puzzle Solver")
        print("Select 1 to use a default puzzle(solution is at depth of 4), or 2 to enter your own puzzle.(Make sure to hit ENTER after every input)")
        puzzle_selection = input("Enter 1 or 2: ")
        if puzzle_selection == "1":
            initial_state = [[1,2,3],[5,0,6],[4,7,8]]#has depth of 2
        elif puzzle_selection == "2":
            print("Enter numbers left to right, top to bottom. Hit ENTER after every number.")
            for i in range(N_PUZZLE):
                for j in range(N_PUZZLE):
                    initial_state[i][j] = input("Enter number (row {}, col {}): ".format(str(i+1), str(j+1)))
        print("Enter 1 to solve with Uniform Cost Search.")
        print("Enter 2 to solve with A* with the Misplaced Tile Heuristic.")
        print("Enter 3 to solve with A* with the Manhattan Distance Heuristic.")
        queueing_function = input("")

        general_search(initial_state, queueing_function)


        


        again = input("Enter 1 to solve another puzzle. Enter 2 to exit")
        if again == 2:
            loop == False

def goal_test(A, B):
    if A == B:
        return True
    else:
        return False

def general_search(problem, queueing_function):
    if queueing_function == 1:
        pass
    elif queueing_function == 2:
    
    elif queueing_function == 3:



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

#general search algorithm
# function general_search(problem, queueing function)
#     nodes = make_queue(make_node(problem.initial_state)))
#     loop do
#         if empty(nodes) then return failure
#         node = remove_front(nodes)
#         if problem.goal_test(node.state) then return node
#         nodes = queueing_function(nodes, expand(node, problem.operators))
#         end

def expand(node, ):


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

