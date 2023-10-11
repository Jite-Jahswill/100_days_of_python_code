print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

player = input("Please Tell us your name. ")
route = input("where do you which to go, Left or Right? ").lower()
means = input("There's a river ahead and a boat coming do you which to swim or wait? ").lower()
door = input("You've arrived at a house with 3 doors of color Red, Yello and Blue which door? ").lower()

if route == "left":
    if means == "wait":
        if door == "yello":
            print(f"You Win player {player}")
else:
    print("Game over")
    
# OR

player = input("Please Tell us your name.\n ")
route = input("where do you which to go, Left or Right? \n ").lower()

if route == "left":
    means = input("There's a river ahead and a boat coming do you which to swim or wait?\n ").lower()
    if means == "wait":
        door = input("You've arrived at a house with 3 doors of color Red, Yello and Blue which door?\n ").lower() 
        if door =="red":
            print(f"{player} Its a room full of fire, you died player")
        elif door== "yello":
            print(f"{player} You found the treasure! you win player")
        elif door == "blue":
            print(f"{player} You enter a room full of beasts. Game Over")
        else:
            print(f"{player} You chose a door that doesn't exist. Game over")
    else:
        print(f"{player} You got attacked by an angry shark. Game Over")
else:
    print(f"{player} You fell into a hole player")