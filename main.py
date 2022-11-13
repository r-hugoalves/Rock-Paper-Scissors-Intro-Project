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
      
check_win('rock', 'rock')
    