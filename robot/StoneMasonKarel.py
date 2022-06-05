from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        build_wall()
        move_to_next_wall()
    build_wall()

def build_wall():
    safe_place_beeper()
    turn_left()
    while front_is_clear():
        move()
        safe_place_beeper()

def move_to_next_wall():
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    for i in range(4):
        move()

def turn_around():
    turn_left()
    turn_left()

def safe_place_beeper():
    if no_beepers_present():
        put_beeper()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
