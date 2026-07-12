def create_grid():
    rows, cols = 13, 13
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
# ALGORITHM (top row)

    word = "ALGORITHM"
    for i in range(len(word)):
        grid[0][2 + i] = word[i]
    # PROGRAMMING (left vertical)
    
    word = "PROGRAMMING"
    for i in range(len(word)):
        grid[1 + i][0] = word[i]

    # COMPUTER (middle vertical)
    word = "COMPUTER"
    for i in range(len(word)):
        grid[3 + i][6] = word[i]

    # LANGUAGE (right vertical)
    word = "LANGUAGE"
    for i in range(len(word)):
        grid[2 + i][11] = word[i]

    # PYTHON (horizontal near bottom)
    word = "PYTHON"
    for i in range(len(word)):
        grid[8][4 + i] = word[i]
    return grid

def display(grid):
    for row in grid:
        print(' '.join(row))

def main():
    grid = create_grid()
    display(grid)
if __name__ == "__main__":
    main()