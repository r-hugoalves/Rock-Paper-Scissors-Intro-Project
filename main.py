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
        # 'choice' é um dicionário / dict = {'key': value, 'key': value}

    return choices

# print(get_choices())