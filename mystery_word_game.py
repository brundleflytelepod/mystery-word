import sys
import random


def get_word_from_file(file):
    """Get's a random word from a list of words in a text file and returns it
    as lowercase string."""
    with open(file) as file:
        file = file.readlines()
        file = [''.join(lines).strip().lower() for lines in file]
        return random.choice(file)


def get_intro(random_word):
    """Prints the introduction to the game and the number of letters in the
    selected word."""
    return("""
            ___  ___          _                    _    _               _
            |  \/  |         | |                  | |  | |             | |
            | .  . |_   _ ___| |_ ___ _ __ _   _  | |  | | ___  _ __ __| |
            | |\/| | | | / __| __/ _ \ '__| | | | | |/\| |/ _ \| '__/ _` |
            | |  | | |_| \__ \ ||  __/ |  | |_| | \  /\  / (_) | | | (_| |
            \_|  |_/\__, |___/\__\___|_|   \__, |  \/  \/ \___/|_|  \__,_|
                     __/ |                  __/ |
                    |___/                  |___/
            \n\n\nI'm thinking of a word with {} letters in it..."""
           .format(len(random_word)))


def get_guess(guess):
    """Accepts and evaluates the user's guess and returns a result."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    guess = guess.lower()
    if guess not in alphabet:
        print("No no no, give me a LETTER! Try again...")
        return None
    elif len(guess) > 1:
        print("Umm, 1 letter at a time please... try again.")
    elif guess not in guessed_letters:
        guessed_letters.append(guess)
        if guess in random_word:
            return True
        elif guess not in random_word:
            return False
    else:
        print("You already guessed that letter... try again.")
        return None


def display_word(random_word, guessed_letters):
    """Iterates through the random word then displays the current progress."""
    display_string = ''
    for letter in random_word:
        if letter in guessed_letters:
            display_string += (letter)
        else:
            display_string += ("_")
    return(display_string)


def turn_flow(turns):
    """Initiates the turn cycle of the game."""
    while turns > 0:
        display = (display_word(random_word, guessed_letters))
        print("\n\n" + display)

        if '_' not in display:
            play_again = input("You win! Do you want to play again?\n(y,n) >:")

            if play_again == 'y' or play_again == 'Y':
                return

            elif play_again == 'n' or play_again == 'N':
                print("Goodbye!!")
                sys.exit()

            else:
                print("I'll take that as a no...goodbye.")
                sys.exit()

        guess = get_guess(input("Guess a single letter...\n>:"))

        if guess is True:
            print("\n\n\nGood guess! You have {} turns left.".format(turns))
            continue

        elif guess is False:
            turns -= 1
            print("\n\n\nI'm sorry, but that is not in my word.")
            print("You have {} turns left.""".format(turns))
            continue

        elif guess is None:
            continue

    print("\n\n\n\nOh no! You ran out of turns! You lose!! Goodbye!!")
    sys.exit()


while True:
    random_word = get_word_from_file("/usr/share/dict/words")
    print(get_intro(random_word))
    print(random_word)
    guessed_letters = []
    turn_flow(8)
