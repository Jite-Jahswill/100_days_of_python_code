# Scopes

##### Local scope
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# or

def drink_portion():
    portion_strength = 2
    print(portion_strength)
    
drink_portion()
# print(portion_strength)
# here portion_strength is a local variable to only the drink_portion function

##### Global scope
player_health = 10
def drink_portion():
    portion_strength = 2
    print(player_health)
drink_portion()
# here player_health is a global variable

# There is no block scope in
game_level = 3
enemies = ["Skeleton","Zombie","Alien"]
if game_level < 5:
    new_enemy = enemies[0]
    
print(new_enemy)
# here new enemy is a global scope because it is an if statement but if
# we place in a function it becomes a local scope.

# How to modify variables with global scope
player_health_1 = 10

def drink_portion():
    global player_health_1
    portion_strength_1 += 2
    print(player_health_1)
drink_portion()

# using global code helps us bring a global variable to our function to help us modify it
# better we use return than the above code to prevent bugs

player_health_1 = 10

def drink_portion():
    print(player_health_1)
    return player_health_1 + 1
player_health_1 = drink_portion()

# Global constants 
PI = 3.14159
URL = "https://www.jw.org"

def calc():
    URL
# using capital letters for variables helps us know constant variable that need not be modified.
################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

