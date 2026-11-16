import heapq

# Represent the 3x3 board as a simple 9-character string ('0' is the blank space)
START = "123560784"
GOAL  = "123586074"

# Pre-defined valid swap positions for each index (0 to 8) on the board
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7],
}

def misplaced_tiles(board):
    """Count how many tiles are NOT in their correct goal spot."""
    count = 0
    for i in range(9):
        if board[i] != '0' and board[i] != GOAL[i]: #Both conditions must be true to count as a mistake.
            count += 1
    return count

def solve_puzzle(start):
    # Priority queue holds: (total_score, steps_taken, current_board, path_history)
    queue = [(misplaced_tiles(start), 0, start, [start])]
    visited = set()

    while queue:
        score, steps, board, path = heapq.heappop(queue)

        # Check if we reached the goal
        if board == GOAL:
            return path

        if board in visited:
            continue
        visited.add(board)

        # Find where the blank space ('0') is
        zero_pos = board.index('0')

        # Try swapping '0' with every valid neighbor
        for neighbor_pos in MOVES[zero_pos]:
            board_list = list(board)
            # Swap the blank space with the neighboring tile
            board_list[zero_pos], board_list[neighbor_pos] = board_list[neighbor_pos], board_list[zero_pos]
            new_board = "".join(board_list)

            if new_board not in visited:
                new_steps = steps + 1
                new_score = new_steps + misplaced_tiles(new_board)
                heapq.heappush(queue, (new_score, new_steps, new_board, path + [new_board]))

# Run the code and print each step nicely
solution = solve_puzzle(START)

for step_num, state in enumerate(solution):
    print(f"--- Step {step_num} ---")
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
