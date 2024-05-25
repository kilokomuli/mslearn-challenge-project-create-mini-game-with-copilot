# # write a 'Hello world' in python
# print("Hello world")

# x = input("Enter your name: ")
# print('Hello, ' + x)
# creates a rock paper scisssors game using python with Github copilot
# import the random module
import random

# create lists of options
choices = ['rock', 'paper', 'scissors']

# create a score and round played variables
score = 0
rounds_played = 0

# create a loop to play the game
while True:
    computer_choice = random.choice(choices)
    player_choice = input('Enter rock, paper, or scissors: ')

    # if player choose rock
    if player_choice.lower() == 'rock':
        if computer_choice == 'rock':
            print('Computer chose rock. It is a tie!')
        elif computer_choice == 'paper':
            print('Computer chose paper. You lose!')
        else:
            print('Computer chose scissors. You win!')
            score += 1
        rounds_played += 1
    
    # if player choose paper
    elif player_choice.lower() == 'paper':
        if computer_choice == 'rock':
            print('Computer chose rock. You win!')
            score += 1
        elif computer_choice == 'paper':
            print('Computer chose paper. It is a tie!')
        else:
            print('Computer chose scissors. You lose!')
        rounds_played += 1

    # if palyer choose scissors
    elif player_choice.lower() == 'scissors':
        if computer_choice == 'rock':
            print('Computer chose rock. You lose!')
        elif computer_choice == 'paper':
            print('Computer chose paper. You win!')
            score += 1
        else:
            print('Computer chose scissors. It is a tie!')
        rounds_played += 1

    # if player choose something else
    else:
        print('Not a valid play, check your spelling!')
    
    # ask if player wants to play again
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() == 'no':
        print('Thanks for playing!')
        print('Your score:', score)
        print('Rounds played:', rounds_played)
        break
    elif play_again.lower() == 'yes':
        continue
    else:
        print('Invalid input. Exiting game.')
        break