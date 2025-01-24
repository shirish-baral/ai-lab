import heapq

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def best_first_search(grid, start, treasure):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = []

    heapq.heappush(pq, (manhattan_distance(*start, *treasure), start))
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)
        x, y = current

        if current == treasure:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < rows and
                0 <= ny < cols and
                (nx, ny) not in visited and
                grid[nx][ny] == 1
            ):
                neighbor = (nx, ny)
                heuristic = manhattan_distance(nx, ny, *treasure)
                heapq.heappush(pq, (heuristic, neighbor))
                if neighbor not in parent:
                    parent[neighbor] = current

    return []

# Input handling
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the grid (1 for paths, 0 for obstacles):")
grid = []
for _ in range(rows):
    grid.append(list(map(int, input().split())))

start_x, start_y = map(int, input("Enter the starting position (row column): ").split())
treasure_x, treasure_y = map(int, input("Enter the treasure position (row column): ").split())

# Validating input positions
if not (0 <= start_x < rows and 0 <= start_y < cols):
    print("Invalid starting position: Out of grid bounds.")
elif not (0 <= treasure_x < rows and 0 <= treasure_y < cols):
    print("Invalid treasure position: Out of grid bounds.")
elif grid[start_x][start_y] != 1:
    print("Invalid starting position: Cannot start on an obstacle.")
elif grid[treasure_x][treasure_y] != 1:
    print("Invalid treasure position: Cannot place treasure on an obstacle.")
else:
    start = (start_x, start_y)
    treasure = (treasure_x, treasure_y)
    path = best_first_search(grid, start, treasure)
    if path:
        print("Path to treasure:", path)
    else:
        print("No path to the treasure was found.")
