print("Welcome to game world")
r = "Rock"
p = "Paper"
s = "Scissor"
limit = 0
cu = 0
cp = 0
name = input("Enter ur name")
print("Game limit is 5 times")

while(limit<5):
    import random
    lst = ["Rock", "Paper", "Scissor"]
    choice = random.choice(lst)
    i = str(input("Please type your choice:\n"
               "1.Rock\n2.Paper\n3.Scissor\n"))
    print("Computer:", choice)
    if choice == r and i == p:
        print("You won"  )
        cu+=1

    elif choice == p and i== r:
        print("Computer won")
        cp+=1

    elif choice == p and i == s:
        print("You won")
        cu += 1

    elif choice == s and i== p:
        print("Computer won")
        cp += 1

    elif choice == s and i == r:
        print("You won")
        cu += 1

    elif choice == r and i== s:
        print("Computer won")
        cp += 1

    elif choice == p and i== p:
        print("Match is Draw")

    elif choice == r and i== r:
        print("Match is Draw")

    elif choice == s and i== s:
        print("Match is Draw")


    else:
        print("Invalid Choice")
        break

    limit+=1
if (cu > cp):
    print(f"\n{name} is the Winner".upper())

else:
    print("\nSorry Computer is a winner".upper())




