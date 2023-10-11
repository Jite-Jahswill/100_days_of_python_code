# Step 1
import random

word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the world_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess.
# Make guess lowercase.

# TODO-3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word


random_pick = random.randint(0, 4)
chosen_word = word_list[random_pick]
# or
chosen_word = random.choice(word_list)





        
# TODO-4 - create an empty list called display
# for each letter in the chosen_word, add a "_" to 'display
# so if the chosen_word was "apple", display should be ["_","_","_","_"."_"]
# with 5 "_"representing each letter to guess.

# TODO-5 - Loop through each position in the chosen_word;
# if the letter at that position matches 'guess' then revel that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# TODO-6 - Print 'display and you should see the guessed letter in the correct position and every other letter repladed
# with "_"

# HINT - Don't worry about getting the user to guess the next letter. we'll tackle that in step 3

display = []
world_length = len(chosen_word)


for letter in chosen_word:
    display += "_"
print(display)


# or
for _ in range(world_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    for position in range(world_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            print("wrong")
            
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")

# TODO-7 - use a while loop to let the user guess again. The loop should only stop once the user guessed all the letters in the 
# chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
