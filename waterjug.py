cap5 = 5 # X jug
cap3 = 3 # Y jug
x = 0 # 5-gallon jug
y = 0 # 3-gallon jug
target = 4
print("WATER JUG PROBLEM")
print("Goal: Get exactly 4 liters in 5L Jug")

while True:
    print("\nCurrent State: (X,Y) =", (x, y))
    # Goal check
    if x == target:
        print("\n🎉 Goal Achieved! 5L Jug contains 4 liters.")
        break
    print("\nChoose Rule Number:")
    print("1. Fill 5-g jug")
    print("2. Empty 5-g jug")
    print("3. Fill 3-g jug")
    print("4. Empty 3-g jug")
    print("5. Empty 3-g into 5-g (X+Y <= 5)")
    print("6. Empty 5-g into 3-g (X+Y <= 3)")
    print("7. Pour 3-g into 5-g until full (X+Y >= 5)")
    print("8. Pour 5-g into 3-g until full (X+Y >= 3)")
    print("9. Exit")
    choice = input("Enter rule number: ")
# Rule 1
    if choice == "1" and x < cap5:
        x = cap5

    # Rule 2
    elif choice == "2" and x > 0:
        x = 0

    # Rule 3
    elif choice == "3" and y < cap3:
        y = cap3

    # Rule 4
    elif choice == "4" and y > 0:
        y = 0

    # Rule 5 (X+Y <= 5 & Y > 0)
    elif choice == "5" and (x + y <= cap5 and y > 0):
        x = x + y
        y = 0

    # Rule 6 (X+Y <= 3 & X > 0)
    elif choice == "6" and (x + y <= cap3 and x > 0):
        y = x + y
        x = 0

    # Rule 7 (X+Y >= 5 & Y > 0)
    elif choice == "7" and (x + y >= cap5 and y > 0):
        y = y - (cap5 - x)
        x = cap5

    # Rule 8 (X+Y >= 3 & X > 0)
    elif choice == "8" and (x + y >= cap3 and x > 0):
        x = x - (cap3 - y)
        y = cap3

    elif choice == "9":
        print("Exited.")
        break
    
    else:
        print("Rule not applicable for current state!")