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

            
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                neighbor = (nx, ny)
                heuristic = manhattan_distance(nx, ny, *treasure)
                heapq.heappush(pq, (heuristic, neighbor))
                if neighbor not in parent:
                    parent[neighbor] = current

    
    return []


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the grid (0 for open cells, other numbers can represent obstacles):")
grid = []
for _ in range(rows):
    grid.append(list(map(int, input().split())))


start_x, start_y = map(int, input("Enter the starting position (x y): ").split())


treasure_x, treasure_y = map(int, input("Enter the treasure position (x y): ").split())


start = (start_x, start_y)
treasure = (treasure_x, treasure_y)

if grid[start_x][start_y] != 0 or grid[treasure_x][treasure_y] != 0:
    print("Invalid starting or treasure position: Cannot start or end on an obstacle.")
else:
    path = best_first_search(grid, start, treasure)
    if path:
        print("Path to treasure:", path)
    else:
        print("No path to the treasure was found.")