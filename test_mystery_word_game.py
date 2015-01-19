import mystery_word_game as myst


word_list = ["aardvark", "aardwolf", "beach",
             "dude", "surf", "train", "umbrella", "zebra"]


def test_get_word_from_file():
    assert myst.get_word_from_file("tester_text_dummy_file.txt") in word_list


def test_get_intro():
    assert myst.get_intro("beer") == """
            ___  ___          _                    _    _               _
            |  \/  |         | |                  | |  | |             | |
            | .  . |_   _ ___| |_ ___ _ __ _   _  | |  | | ___  _ __ __| |
            | |\/| | | | / __| __/ _ \ '__| | | | | |/\| |/ _ \| '__/ _` |
            | |  | | |_| \__ \ ||  __/ |  | |_| | \  /\  / (_) | | | (_| |
            \_|  |_/\__, |___/\__\___|_|   \__, |  \/  \/ \___/|_|  \__,_|
                     __/ |                  __/ |
                    |___/                  |___/
            \n\n\nI'm thinking of a word with 4 letters in it..."""


#def test_get_guess():
#    random_word = 'beer'
#    guessed_letters = ['b']
#    assert myst.get_guess('e') is True
#    assert myst.get_guess('a') is False
#    assert myst.get_guess('1') is None
#    assert must.get_guess('b') is None
# I'm guessing my problem here is weak function design, these fail because they
# depend on outside variable assignment, not sure of a workaround
# also at a loss on how to test my turn_flow() function

def test_display_word():
    assert myst.display_word('beer', ['b', 'r']) == "b__r"
