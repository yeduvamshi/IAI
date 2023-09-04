import heapq

def ucs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    def is_valid(x, y):
        return 0 <= x < r and 0 <= y < c and grid[x][y] != '%'

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    visited = set()
    queue = [(0, pacman_r, pacman_c, [])]

    while queue:
        cost, x, y, path = heapq.heappop(queue)

        if x == food_r and y == food_c:
            return cost, path

        if (x, y) not in visited:
            visited.add((x, y))
            for nx, ny in get_neighbors(x, y):
                heapq.heappush(queue, (cost + 1, nx, ny, path + [(nx, ny)]))

def nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    cost, path = ucs(r, c, pacman_r, pacman_c, food_r, food_c, grid)

    # Print distance
    print(cost)

    # Print path
    for x, y in path:
        print(x, y)

# Sample Input
pacman_r, pacman_c = map(int, input().split())
food_r, food_c = map(int, input().split())
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]

nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)
