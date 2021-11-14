# package: Hangman
# Created by: Noel Nagy
# Website: https://github.com/nagynooel

import configparser
import os.path
import random

# -- Global variables
is_first_start: bool
username: str
difficulty: int
max_tries: int
wordlist: str

# Maximum length of the words by difficulty. Hard has no limit. 
easy_length: int = 5
medium_length: int = 10

# These are the settings used if the game is unable to load in/create the settings.ini file.
default_settings: list[str:str] = {"is_first_start":"1", "username":"guest","difficulty":"0", "max_tries":"5" ,"wordlist":".\wordlist.txt"}

# -- Functions
# Read settings file if exsists, otherwise create default config file.
config = configparser.ConfigParser()
config.read("settings.ini")
def get_settings() -> None:
    # If settings.ini doesn't exist, make new one with default settings!
    if not os.path.isfile(".\settings.ini"):
        config["MAIN"] = default_settings
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
    
    global is_first_start
    global username
    global difficulty
    global max_tries
    global wordlist
    try:
        is_first_start = bool(int(config["MAIN"]["is_first_start"]))
        username = config["MAIN"]["username"]
        difficulty = int(config["MAIN"]["difficulty"])
        max_tries = int(config["MAIN"]["max_tries"])
        wordlist = config["MAIN"]["wordlist"]
    except:
        # If an error occoures while reading the settings.ini revert tu default settings.
        print("Error loading in settings! Reverting to default settings. Please check the integrity of the settings.ini and try again. If nothing else works delete the settings.ini file and reload script.")
        is_first_start = bool(int(default_settings["is_first_start"]))
        username = default_settings["username"]
        difficulty = default_settings["difficulty"]
        max_tries = default_settings["max_tries"]
        wordlist = default_settings["wordlist"]

# Update the values of the settings in settings.ini
def update_settings() -> None:
    try:
        config["MAIN"]["is_first_start"] = str(int(is_first_start))
        config["MAIN"]["username"] = username
        config["MAIN"]["difficulty"] = str(difficulty)
        config["MAIN"]["max_tries"] = str(max_tries)
        config["MAIN"]["wordlist"] = wordlist
        with open('settings.ini', 'w') as configfile:
                config.write(configfile)
    except:
        print("FAILED to update settings in the settings.ini file.")
        get_settings()

# Get user input for a menu and return the selected number between the 2 parameters.
def get_menu_user_input(start_num, end_num) -> int:
    inp = start_num-1
    while inp < start_num or inp > end_num:
        try:
            inp = int(input("Number of button/setting: "))
            if inp < start_num or inp > end_num:
                raise Exception()
        except:
            print("Please give a valid input!\n")
    return inp

# Get a string type input from the user until it is not empty and input is in the available options list(if list is not empty).
def get_string_user_input(input_text: str = "Letter: ", check_if_more_chars: bool = True, error_msg: str = "Input needs to be only 1 letter!", available_options: list[str] = []) -> str:
    inp = ""
    while inp == "" or inp == " ":
        try:
            inp = input("\n" + input_text)
            if (check_if_more_chars and len(inp) > 1) or inp == "" or inp == " " or (len(available_options) != 0 and inp not in available_options):
                inp = ""
                raise Exception()
        except:
            print(error_msg)
    return inp

# Settings page functions
# Difficulty levels: Easy - 0 Normal - 1 Hard - 2
# Easy maximum word length: 5
# Normal maximum word length: 10
# Hard maximum word length: no limit
def set_difficulty(difficulty: int) -> None:
    pass

# Modifiy wordlist file
def modify_wordlist(new_wordlist_name: str) -> None:
    pass

# Add/Remove word to/from wordlist
def add_word(word: str) -> None:
    pass

def remove_word(word: str) -> None:
    pass

# -- Pages
def start_game() -> None:
    # Select the word based on difficulty
    file = open(wordlist, "r")
    words = file.readlines()
    word: str = words[random.randint(0, len(words)-1)][:-1]
    if difficulty == 0:
        while len(word) > easy_length:
            word = words[random.randint(0, len(words)-1)][:-1]
    elif difficulty == 1:
        while len(word) > medium_length or len(word) <= easy_length:
            word = words[random.randint(0, len(words)-1)][:-1]
    else:
        while len(word) <= medium_length:
            word = words[random.randint(0, len(words)-1)][:-1]
    # Establish basic variables
    word_length: int = len(word)
    tries: int = max_tries
    guessed: str = ""
    for _ in range(word_length):
        guessed += "_"
    # Start the game
    print("\n\n-Game started-")
    print(f"Length of the word: {word_length}")
    print(f"Good luck {username}!")
    # Main game loop
    while guessed != word and tries > 0:
        print(f"\nNumber of tries left: {tries}\n")
        # Print out the current state of the game with spaces between letters
        for guessed_letter in guessed:
            print(guessed_letter, end=" ")
        print("\n")
        guess: str = get_string_user_input()
        # Check that the guessed letter is in the word and that the letter haven't been guessed yet
        if guess in word and guess not in guessed:
            number_of_occurrence: int = 0
            for ind, let in enumerate(word):
                if let == guess:
                    guessed = guessed[:ind] + let + guessed[ind+1:]
                    number_of_occurrence += 1
            if number_of_occurrence == 1:
                print(f"\n\n\nThe letter {guess} appers 1 time in the word!")
            else:
                print(f"\n\n\nThe letter {guess} appers {number_of_occurrence} time(s) in the word!")
        elif guess in word and guess in guessed:
            print(f"\n\n\nU already found the letter {guess}!")
        else:
            tries -= 1
            print(f"\n\n\nThe letter {guess} is not in the word!")
    # Decide the outcome of the game
    if guessed == word:
        print(f"\nCongratulations! You found the word \"{word}\"")
        print(f"You had {tries} tries left!")
    else:
        print(f"\nYou ran out of tries! The word was \"{word}\"")
    inp = get_string_user_input("Would you like to play the game again? (y/n)", True, "Please enter \"y\" or \"n\" only!", ["y","n"])
    if inp == "y":
        start_game()

def stats_page() -> None:
    pass

def settings_page() -> None:
    pass

# Main menu
def main_menu_page() -> None:
    # If this is the user's first time playing the game, ask for a username
    global is_first_start
    if is_first_start:
        global username
        print("\n\n--Welcome to the hangman console game!--")
        print("Created by: Noel Nagy")
        print("\nWe see that you are new to this game(or reseted the settings)! Please enter your name to get started!")
        inp = get_string_user_input("Username: ", False, "Your name can't be blank! Please input a valid username.", [])
        username = inp
        is_first_start = False
        print(f"\nHey {username}! If you enjoy the game please leave a revive on my github page! Have fun! https://github.com/nagynooel/Hangman\n")
        update_settings()

    # This is the main loop for the game. If this ends the script will stop running.
    while True:
        print("\n\n--Welcome to the hangman console game!--")
        print("Created by: Noel Nagy")
        print("\n-Main menu-")
        print("\nType the number of the button that you'd like to select!")
        print("1 Play Game")
        print("2 Statistics")
        print("3 Settings")
        print("4 Exit\n")
        
        inp = get_menu_user_input(1,4)
        # Handle input
        if inp == 1:
            start_game()
        elif inp == 2:
            stats_page()
        elif inp == 3:
            settings_page()
        elif inp == 4:
            exit()

if __name__ == "__main__":
    get_settings()
    main_menu_page()