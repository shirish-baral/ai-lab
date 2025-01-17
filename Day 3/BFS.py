from collections import deque

def get_maze_input():
    print("Enter the number of rows and columns in the maze:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print("Enter maze values:")
    maze = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for cell ({i}, {j}): "))
            row.append(value)
        maze.append(row)
    return maze

def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))

    return -1

if __name__ == "__main__":
    maze = get_maze_input()
    print("Enter the start position (row and column, 0-indexed):")
    start_row = int(input("Start row: "))
    start_col = int(input("Start column: "))
    start = (start_row, start_col)

    print("Enter the end position (row and column, 0-indexed):")
    end_row = int(input("End row: "))
    end_col = int(input("End column: "))
    end = (end_row, end_col)

    shortest_path = bfs_maze_solver(maze, start, end)

    if shortest_path != -1:
        print(f"The shortest path from {start} to {end} is {shortest_path} steps.")
    else:
        print("No path exists between the start and end points.")
