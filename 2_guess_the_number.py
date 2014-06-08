{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf190
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 # template for "Guess the number" mini-project\
# input will come from buttons and an input field\
# all output for the game will be printed in the console\
\
import simplegui\
import random\
import math\
\
# initialize global variables used in your code\
game_of_100 = True #default\
maximum = 100 #default value\
remaining_guesses = None #default value\
secret_number = None #default value\
\
\
# helper function to start and restart the game\
def new_game():   \
    global remaining_guesses, secret_number\
    if game_of_100:\
        remaining_guesses = 7\
    else:\
        remaining_guesses = 10\
        \
    secret_number = random.randrange(0, maximum)\
    print "New game. Range is from 0 to " + str(maximum)\
    print "Number of remaining guesses " + str(remaining_guesses)\
    print\
        \
\
# define event handlers for control panel\
def range100():\
    # button that changes range to range [0,100) and restarts\
    global game_of_100, maximum\
    game_of_100 = True\
    maximum = 100\
    new_game()\
\
def range1000():\
    # button that changes range to range [0,1000) and restarts\
    global game_of_100, maximum\
    game_of_100 = False\
    maximum = 1000\
    new_game()\
    \
def input_guess(guess):\
    global remaining_guesses, secret_number\
    if remaining_guesses > 0:\
        remaining_guesses -= 1\
   \
    print "Guess was " + guess\
    print "Number of remaining guesses is " + str(remaining_guesses)\
    guess = float(guess)\
    \
    if guess == secret_number:\
        print "Correct!"\
        print\
        new_game()\
    elif remaining_guesses == 0:\
        print "You ran out of guesses. The number was " + str(secret_number)\
        print\
        new_game()\
    elif guess > secret_number:\
        print "Lower"\
    else:\
       print "Higher"\
    print\
\
    \
# create frame\
f = simplegui.create_frame("Guess the number", 200, 200)\
\
\
# register event handlers for control elements\
f.add_button("Range is [0, 100)", range100, 200)\
f.add_button("Range is [0, 1000)", range1000, 200)\
f.add_input("Enter a guess", input_guess, 200)\
\
\
# call new_game and start frame\
new_game()\
f.start()\
\
\
# always remember to check your completed program against the grading rubric\
}