# Rock-Paper-Scissor Intro Project / Projeto Introdutório: Pedra, Papel e Tesoura #
# FreeCodeCamp
# Hugo R. Alves https://github.com/r-hugoalves/Rock-Paper-Scissors-Intro-Project

            # Funções e Variáveis / Variables and Functions #

import random

def get_choices():
    player_choice = input('Enter a choice (rock, papel, scissors): ')
    options = ['paper', 'rock', 'scissors']
    computer_choice = random.choice(options)

    choices = {'player': player_choice, 'computer': computer_choice}
        # 'choice' is a dictionarie / dict = {'key': value, 'key': value}

    return choices

# print(get_choices())

def check_win(player, computer):
    print('You chose: ' + player)
    print(f'Computer chose: {computer}')

    if player == computer:
        print('It is a tie!')
    elif player == 'rock' and computer == 'paper':
        print('Computer wins!')
    elif player == 'rock' and computer == 'scissors':
        print('Player wins!')

    elif player == 'paper' and computer == 'rock':
        print('Player wins!')
    elif player == 'paper' and computer == 'scissors':
        print('Computer wins!')

    elif player == 'scissors' and computer == 'paper':
        print('Player wins!')
    elif player == 'scissors' and computer == 'rock':
        print('Computer wins!')
    
# We can also do with a if whithin the elif statement. Example: 

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

    