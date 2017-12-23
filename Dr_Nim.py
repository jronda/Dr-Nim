#
# Dr. Nims game inspired by Matt Parker
#
# At this point the computer always wins
#
import random
from time import sleep

def DrNim(bits):
    """ Playes the game Dr. Nim """

    print ("OK, let's play!", '\n')
    print("The bits to start:", bits)
    board = bits * 'X'
    print(board)
    print()

    while True:

        bits = player(bits)
        if bits == 0:
            print("You win, I lose.")
            break
        else:
            print("The bits left:", bits)
            print(bits * 'X')
            print()
        
        bits = AI(bits)
        if bits == None:
            print("I win, you lose.")
            break
        else:
            print("The bits left:", bits)
            print(bits * 'X')
            print()
        

def player(bits):
    """ Plays the game as a player """

    print("Your turn.")
    while True:
        choice = int(input("How many do you want to take away? "))
        print()

        if choice in [1,2,3]:
            print("You take", choice, "away from", bits)
            length = bits - choice
            return length
        else:
            print("Try agian, must be 1 or 2 or 3")
            print()

    return bits

def AI(bits):
    """ Plays the game as an AI """

    x = random.randint(0, 6)
    sleep(x * .25)

    length = bits
    if length < 4:
        bits = bits
        print("I'm taking away the last", bits, "to win.")
        return None
    elif length % 4 == 1:
        bits -= 1
        print("I'm taking away", 1, "from", length)
    elif length % 4 == 2:
        bits -= 2
        print("I'm taking away", 2, "from", length)
    elif length % 4 == 3:
        bits -= 3
        print("I'm taking away", 3, "from", length)
        
    return bits
    

def choice():

    while True:

        mode = input("Easy, Medium, Hard, Rules: ").lower()
        
        if mode in ['easy', 'e', 'ez', 'eas', 'ease']:
            DrNim(12)
            break
        elif mode in ['med', 'medium', 'm', 'medi', 'medum']:
            DrNim(16)
            break
        elif mode in ['hard', 'hrd', 'h', 'har', 'ard', 'hd']:
            DrNim(24)
            break
        elif mode == 'rules':
            print()
            print("The Rules:")
            print("We start with a certian number of bits.")
            print("(Easy = 12, Medium = 16, Hard = 24).")
            print("We each can take at least one and up to three away.")
            print("The person, or computer, that removes the last bit wins.", '\n')


print("Welcome to Dr. Nim.", '\n')
print("Select a mode:")
choice()

