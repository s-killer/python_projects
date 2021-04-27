# This program simulated 1 dice rolling

# Logic
# Generates a random number between 1 - 6
# prints the number 
# Show the dice with number in UI


# Todo
# Add UI
# add more instructions

import random


def print_instructions(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run():
    number = number = random.randint(1, 6)
    print("The number is {}".format(number))


def start():
    print_instructions('Hi there!! This is a Rolling Dice simulator.\n Press Ctrl + c to exit')

    # accepting "Y" and "y" to continue
    # converting input to lower case
    while True:

        # accept user input
        to_continue = input("Press Y to roll the dice:\n")
        if to_continue.lower() == "y":
            run()
        else:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
