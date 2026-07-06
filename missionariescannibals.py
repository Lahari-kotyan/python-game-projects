ML = 3
CL = 3
MR = 0
CR = 0
boat = "Left"
print("Missionaries and Cannibals Problem")
while True:
    print("\nLeft Side -> Missionaries:", ML, "Cannibals:", CL)
    print("Right Side -> Missionaries:", MR, "Cannibals:", CR)
    print("Boat:", boat)
    if ML == 0 and CL == 0:
        print("\nGoal Achieved! Everyone crossed safely.")
        break
    print("\nChoose Move")
    print("1. 1 Missionary cross")
    print("2. 1 Cannibal cross")
    print("3. 2 Missionaries cross")
    print("4. 2 Cannibals cross")
    print("5. 1 Missionary and 1 Cannibal cross")
    choice = int(input("Enter choice: "))
    missionaries = 0
    cannibals = 0
    if choice == 1:
        missionaries = 1
    elif choice == 2:
        cannibals = 1
    elif choice == 3:
        missionaries = 2
    elif choice == 4:
        cannibals = 2
    elif choice == 5:
        missionaries = 1
        cannibals = 1
    else:
        print("Invalid choice")
        continue
    # Save current state (in case move is invalid)

    tempML = ML
    tempCL = CL
    tempMR = MR
    tempCR = CR
    tempBoat = boat
    if boat == "Left":
        if missionaries > ML or cannibals > CL:
            print("Not enough people on Left side")
            continue
        ML -= missionaries
        CL -= cannibals
        MR += missionaries
        CR += cannibals
        boat = "Right"
    else:
        if missionaries > MR or cannibals > CR:
            print("Not enough people on Right side")
            continue
        ML += missionaries
        CL += cannibals
        MR -= missionaries
        CR -= cannibals
        boat = "Left"
    # Safety check
    if (ML > 0 and CL > ML) or (MR > 0 and CR > MR):
        print("Unsafe move! Cannibals would eat missionaries.")
        print("Move cancelled. Try another move.\n")
        ML = tempML
        CL = tempCL
        MR = tempMR
        CR = tempCR
        boat = tempBoat