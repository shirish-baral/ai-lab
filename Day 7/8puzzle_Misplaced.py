import heapq
import numpy as np

class PuzzleState:
    def __init__(self, board, parent=None, move="", g=0, h=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g  # Cost from start node
        self.h = h  # Heuristic cost
        self.f = g + h  # Total estimated cost

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return np.array_equal(self.board, other.board)

    def get_neighbors(self):
        neighbors = []
        x, y = np.where(self.board == 0)
        x, y = x[0], y[0]
        moves = [(x-1, y, "Up"), (x+1, y, "Down"), (x, y-1, "Left"), (x, y+1, "Right")]

        for nx, ny, move in moves:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = self.board.copy()
                new_board[x, y], new_board[nx, ny] = new_board[nx, ny], new_board[x, y]
                neighbors.append(PuzzleState(new_board, self, move, self.g + 1))

        return neighbors

def heuristic_misplaced(state, goal):
    return np.sum(state.board != goal) - 1  # Ignore the blank tile

# def heuristic_manhattan(state, goal):
#     cost = 0
#     for num in range(1, 9):
#         x1, y1 = np.where(state.board == num)
#         x2, y2 = np.where(goal == num)
#         cost += abs(x1 - x2) + abs(y1 - y2)
#     return cost

def a_star(start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, start)
    closed_set = set()
    explored_nodes = 0

    while open_list:
        current = heapq.heappop(open_list)
        explored_nodes += 1

        if np.array_equal(current.board, goal):
            path = []
            while current:
                path.append(current.move)
                current = current.parent
            return path[::-1][1:], explored_nodes

        closed_set.add(tuple(map(tuple, current.board)))
        for neighbor in current.get_neighbors():
            if tuple(map(tuple, neighbor.board)) in closed_set:
                continue
            neighbor.h = heuristic(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
            heapq.heappush(open_list, neighbor)

    return None, explored_nodes

if __name__ == "__main__":
    start_board = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    goal_board = np.array([[0,1,2], [3,4,5], [6,7,8]])

    start_state = PuzzleState(start_board, g=0, h=0)

    solution_h1, nodes_h1 = a_star(start_state, goal_board, heuristic_misplaced)
    # solution_h2, nodes_h2 = a_star(start_state, goal_board, heuristic_manhattan)

    print("Solution using Misplaced Tile Heuristic:", solution_h1)
    print("Nodes explored:", nodes_h1)

    # print("Solution using Manhattan Distance Heuristic:", solution_h2)
    # print("Nodes explored:", nodes_h2)