# Rock-Paper-Scissor Intro Project / Projeto Introdutório: Pedra, Papel e Tesoura #
# FreeCodeCamp
# Hugo R. Alves https://github.com/r-hugoalves/Rock-Paper-Scissors-Intro-Project

# Defining the choices of the game #

import random

def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['paper', 'rock', 'scissors']
    computer_choice = random.choice(options)

    choices = {'player': player_choice, 'computer': computer_choice}
        # 'choice' is a dictionarie / dict = {'key': value, 'key': value}

    return choices

# print(get_choices())

# Defining the possibilities of the game #

def check_win(player, computer):
    print('You chose: ' + player)
    print(f'Computer chose: {computer}')

    if player == computer:
        return('It is a tie!')
    elif player == 'rock' and computer == 'paper':
        return('Computer wins!')
    elif player == 'rock' and computer == 'scissors':
        return('Player wins!')

    elif player == 'paper' and computer == 'rock':
        return('Player wins!')
    elif player == 'paper' and computer == 'scissors':
        return('Computer wins!')

    elif player == 'scissors' and computer == 'paper':
        return('Player wins!')
    elif player == 'scissors' and computer == 'rock':
        return('Computer wins!')
    
# We can also do with a 'if' whithin the 'elif' statement. Example: 

#   if player == computer:
#        print('It is a tie!')
#       elif player == 'rock':
#            if computer == 'paper':
#               print('Computer wins!')
#           else:
#                print('Player wins!')
#
#       elif player == 'paper':
#           if computer == 'rock':
#               print('Player wins!')
#           else: 
#               print('Computer wins!')
#
#       elif player == 'scissors':
#           if computer == 'paper':
#               print('Player wins!')
#           else:
#               print('Computer wins!')

# Playing the game #
choices = get_choices()
    # here we define the options of the dictionarie, so we can use the values outside of the function
result = check_win(choices['player'], choices['computer'])
    # here we call the keys of the dictionarie, it means that, we can access the values, wich are now define above
print(result)