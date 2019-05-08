#! /usr/bin/python3-64
"""The main file to have the game run so that one can play.
The shebangs line, line 1, enables this file to be ran using python3 on a 64 bit system.
Enabling Unix/Unix-Like systems to also use the file.(Note: Will attempt to run this way,
not a sure fire way of hacking/willing something to work somewhere it can-not...)

ML Library to play after finished, use library>create badass superbot.

Besides the actual game mechanics, most of the navigation is complete. Needs more bulletproofing,
but will be alright for me to test things out.
"""


from time import sleep
import os, sys
import random as rm
# import ArrowMap
from MemRules import arrow_rules


def display_menu(menu):
    """What the player sees as options/menus to choose from. Two different
    menus will be available."""
    if menu == 'prior':
        print("""\tWelcome to the best(non-curses) game on a windows machine!
        \n\tThe name of the game is Find The Arrow!
        But, as always, there is a small but significant catch...
        The area I left it in has been covered up with idiotic:
        \t\t\tHASHMARKS!!!!!!""")
        print("Can you help me find it?")
        # sleep(3)
        print("Great! I knew you would help!!")
        print("Menu:\n1.Rules\n2.Start Game\n3.Play Different Game\n4.Exit Game\n")

    elif menu == 'main':
        print("Menu:\n1.Rules\n2.Start Game\n3.Play Different Game\n4.Exit Game\n")

    elif menu == 'playing':
        print("1. Reveal Single\n2. Reveal 4x4\n3. Divide Area\n4. Quit Game\n0. Back to Main Menu")


def aliens():
    """Will start the simple alien shooter game from pygame."""
    os.system('Aliens_pygame.bat')


def player_selected(menu):
    """Allows the player to select which option from a menu to choose, then
    executes the chosen option."""
    initial = {'rules': arrow_rules, 'start': start_new_game, 'different': aliens, 'quit': sys.exit,
    '1': arrow_rules, '2': start_new_game, '3': aliens, '4': sys.exit}
    # If 4 or quit is selected in the game, needs to ask if sure before exit.
    in_game = {'1': '', '2': '', '3': '', 'quit': sys.exit, '4': sys.exit, '0': main}

    chosen = str(input('Choose an option: \n##-->>'))
    if menu == 'playing':
        if chosen.lower() in in_game.keys():
            in_game[chosen]()
        elif chosen.lower() not in in_game.keys():
            print("Not a valid option. Try using a number instead.")
        return chosen
    else:
        if chosen.lower() in initial.keys():
            initial[chosen]()
        elif chosen.lower() not in initial.keys():
            print("Not a valid option. Try using a number instead.")
        return chosen

def game_moves():
    """All of what happens for each move a player in_game can use/do."""



def start_new_game():
    """Will allow a new game to begin from the absolute beginning."""
    with open('ArrowMap.txt', 'r') as map:
        for line in map:
            if line == '\n':
                break
            print(line)
    display_menu('playing')
    player_selected('playing')


def main():
    """Will consist of a 'map', an area for user input and a refresh 'apparautus'"""
    final = ['2', '4', 'quit', 'exit', 'stop']


    # display_menu('prior')
    # while player_selected('prior') not in final:
    #     display_menu('main')
    #     pass
