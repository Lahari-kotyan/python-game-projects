print("NIM GAME")
print("1. Single Pile Nim")
print("2. Multi Pile Nim")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    stones = 10
    player = 1
    while stones > 0:
        print("\nStones remaining:", stones)
        move = int(input("Player " + str(player) + ", how many stones to remove: "))
        if move >= 1 and move <= stones:
            stones = stones - move
        else:
            print("Invalid move. Enter between 1 and", stones)
            continue
        if stones == 0:
            print("Player", player, "wins!")
            break
        if player == 1:
            player = 2
        else:
            player = 1

elif choice == 2:
    piles = [3, 5, 7]
    player = 1
    while sum(piles) > 0:
        print("\nCurrent piles:")
        for i in range(len(piles)):
            print("Row", i+1, ":", piles[i])
        row = int(input("Player " + str(player) + " choose row: ")) - 1
        remove = int(input("How many to remove: "))
        if row >= 0 and row < len(piles) and piles[row] >= remove and remove > 0:
            piles[row] -= remove
        else:
            print("Invalid move")
            continue
        if sum(piles) == 0:
            print("Player", player, "wins!")
            break
        player = 2 if player == 1 else 1
else:
    print("Invalid choice. Restart the game.")