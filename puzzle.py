import heapq

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic: Count misplaced tiles
def h(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Find the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# Convert list to tuple for hashing
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Search
def astar(start):
    open_list = []
    heapq.heappush(open_list, (h(start), start, 0))

    visited = set()

    while open_list:
        f, state, g = heapq.heappop(open_list)

        print("Current State:")
        for row in state:
            print(row)
        print("------")

        if state == goal:
            print("Goal Reached!")
            return

        state_tuple = to_tuple(state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        for neighbor in get_neighbors(state):
            if to_tuple(neighbor) not in visited:
                g_new = g + 1
                f_new = g_new + h(neighbor)
                heapq.heappush(open_list, (f_new, neighbor, g_new))

    print("No solution found")

# Example input
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

astar(start)