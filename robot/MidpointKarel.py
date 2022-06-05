from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    put_beeper()
    move_to_wall()
    safe_put()
    turn_around()
    safe_pickup()
    safe_move()
    safe_put()
    safe_move()
    while no_beepers_present():
        move_and_place()
    if front_is_clear():
        pick_beeper()

def move_and_place():
    safe_move()
    while no_beepers_present():
        move()
    safe_pickup()
    turn_around()
    safe_move()
    safe_put()
    safe_move()

def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def safe_pickup():
    if beepers_present():
        pick_beeper()

def safe_move():
    if front_is_clear():
        move()

def safe_put():
    if no_beepers_present():
        put_beeper()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
