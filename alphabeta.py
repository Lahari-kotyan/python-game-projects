tree = [3, 5, 6, 9, 1, 2, 0, -1]
def alphabeta(i, depth, alpha, beta, isMax):
# Leaf node
    if depth == 3:
        return tree[i]
    if isMax:
        best = -1000
        for j in range(2):
            val = alphabeta(2*i + j, depth+1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if alpha >= beta:
                print("Pruned at MAX")
                break
        return best
    else:
        best = 1000
        for j in range(2):
            val = alphabeta(2*i + j, depth+1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if alpha >= beta:
                print("Pruned at MIN")
                break
        return best

    # Display Tree

print("Game Tree:")
print(" MAX")
print(" / \\")
print(" MIN MIN")
print(" / \\ / \\")
print(" MAX MAX MAX MAX")
print(" / \\ / \\ / \\ / \\")
print("3 5 6 9 1 2 0 -1")
    # Run
result = alphabeta(0, 0, -1000, 1000, True)
print("\nOptimal Value:", result)