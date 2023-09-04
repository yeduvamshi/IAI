def displayPathtoPrincess(n, grid):
    m_pos = None
    p_pos = None

    # Find the positions of 'm' (bot) and 'p' (princess) on the grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                m_pos = (i, j)
            elif grid[i][j] == 'p':
                p_pos = (i, j)

    # Calculate the row and column differences between the bot's and princess's positions
    row_diff = m_pos[0] - p_pos[0]
    col_diff = m_pos[1] - p_pos[1]

    # Determine the directions for row and column movements
    row_direction = "UP" if row_diff > 0 else "DOWN"
    col_direction = "LEFT" if col_diff > 0 else "RIGHT"

    # Move vertically (UP or DOWN) first and then horizontally (LEFT or RIGHT)
    moves = [row_direction] * abs(row_diff) + [col_direction] * abs(col_diff)

    # Print the moves
    for move in moves:
        print(move)

# Read input
n = int(input())
grid = [input() for _ in range(n)]

# Call the function to rescue the princess
displayPathtoPrincess(n, grid)
