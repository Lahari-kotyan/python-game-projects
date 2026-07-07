def is_safe(board, row, col, n):
# check column
    for i in range(row):
        if board[i] == col:
            return False
# check diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve(board, row, n):
    if row == n:
        print_solution(board, n)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n)

def print_solution(board, n):
    print("\nSolution:")
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
# Interactive input

n = int(input("Enter number of queens (N): "))
board = [-1] * n
solve(board, 0, n)