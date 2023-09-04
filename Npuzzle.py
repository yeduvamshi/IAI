def solve_n_puzzle(initial_state, k):
    goal_state = [[i * k + j + 1 for j in range(k)] for i in range(k)]
    goal_state[k - 1][k - 1] = 0
   
    def heuristic(state):
        distance = 0
        for i in range(k):
            for j in range(k):
                if state[i][j] != 0:
                    num = state[i][j] - 1
                    row, col = num // k, num % k
                    distance += abs(i - row) + abs(j - col)
        return distance
   
    def possible_moves(x, y):
        moves = []
        if x > 0:
            moves.append(('UP', x - 1, y))
        if x < k - 1:
            moves.append(('DOWN', x + 1, y))
        if y > 0:
            moves.append(('LEFT', x, y - 1))
        if y < k - 1:
            moves.append(('RIGHT', x, y + 1))
        return moves
   
    def apply_move(state, move):
        direction, new_x, new_y = move
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state
   
    open_set = [(heuristic(initial_state), 0, initial_state)]
    closed_set = set([tuple(map(tuple, initial_state))])
   
    while open_set:
        _, moves, current_state = open_set.pop(0)
       
        if current_state == goal_state:
            return moves
       
        x, y = next((i, j) for i in range(k) for j in range(k) if current_state[i][j] == 0)
       
        for move in possible_moves(x, y):
            new_state = apply_move(current_state, move)
            if tuple(map(tuple, new_state)) not in closed_set:
                open_set.append((heuristic(new_state) + moves + 1, moves + 1, new_state))
                closed_set.add(tuple(map(tuple, new_state)))
   
    return -1

# Sample input
k = 3
initial_state = [
    [0, 3, 8],
    [4, 1, 7],
    [2, 6, 5]
]

# Solve N-Puzzle
num_moves = solve_n_puzzle(initial_state, k)

if num_moves == -1:
    print("This puzzle is not solvable.")
else:
    print(num_moves)
