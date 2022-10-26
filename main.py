
#general search algorithm
# function genearl-search(problem, queueing function)
#     nodes = make-queue(make-node(problem.initial-state)))
#     loop do
#         if empty(nodes) then return failure
#         node = remove-front(nodes)
#         if problem.goal-test(node.state) then return node
#         nodes = queueing-function(nodes, expand(node, problem.operators))
#         end



from collections import deque

def main():
    loop = True
    while loop:
        puzzle = [[0 for i in range(3)] for j in range(3)]
        print("Eight Puzzle Solver")
        print("Select 1 to use a default puzzle(depth of 2), or 2 to enter your own puzzle.(Make sure to hit ENTER after ever input)")
        puzzle_selection = input("Enter 1 or 2: ")
        if puzzle_selection == "1":
            initial-state = [[1,2,3],[4,5,6],[0,7,8]]#has depth of 2
        elif puzzle_selection == "2":
            print("Enter the numbers of the puzzle from left to right, top to bottom. Hit ENTER once you've entered every number.")
            for i in range(3):
                for j in range(3):
                    puzzle[i][j] = input("Enter number: ")


goal-state = [[1,2,3],[4,5,6],[7,8,0]]

def goal-test(A, B):
    if A == B:
        return True
    else:
        return False

def general-search(problem, queueing-function):

    nodes = deque()
    #add initial state to deque
    nodes.append(initial-state)

    while True:
        if len(nodes) == 0:
            return "failure"
        node = nodes.popleft()
        if goal-test(node, goal-state):
            return node
        nodes = queueing-function(nodes, expand(node, problem.operators))



if __name__ == "__main__":
    main()

