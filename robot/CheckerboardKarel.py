from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    # Handle the special case for 1 column
    if front_is_blocked():
        put_beeper()
        turn_left()
        while front_is_clear():
            move()
            move_put_beeper()
        turn_around()
        move_to_wall()
    while no_beepers_present():
        fill_and_back()
        turn_right()
        if front_is_clear():
            move()
            if front_is_clear():
                move()
                turn_right()
            else:
                turn_right()
                move_to_wall()
                turn_around()
    # Handle odd sized boards
    turn_around()
    while front_is_clear():
        move()
        turn_left()
        fill_odd_size()
        turn_left()
        if front_is_clear():
            move()

def fill_odd_size():
    while front_is_clear():
        move_put_beeper()
        if front_is_clear():
            move()
    turn_around()
    while front_is_clear():
        move()

def move_to_wall():
    while front_is_clear():
        move()

def fill_and_back():
    put_beeper()
    while front_is_clear():
        move()
        move_put_beeper()
    turn_around()
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def move_put_beeper():
    if front_is_clear():
        move()
        if no_beepers_present():
            put_beeper()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
