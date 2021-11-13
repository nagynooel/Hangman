# package: Hangman
# Created by: Noel Nagy
# Website: https://github.com/nagynooel

import configparser
import os.path

# -- Global variables
is_first_start: bool
username: str
difficulty: int
max_tries: int
wordlist: str

# These are the settings used if the game is unable to load in/create the settings.ini file.
default_settings: list[str:str] = {"is_first_start":"1", "username":"guest","difficulty":"0", "max_tries":"5" ,"wordlist_path":".\\", "wordlist_filename":"wordlist.txt"}

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
        wordlist = config["MAIN"]["wordlist_path"] + config["MAIN"]["wordlist_filename"]
    except:
        # If an error occoures while reading the settings.ini revert tu default settings.
        print("Error loading in settings! Reverting to default settings. Please check the integrity of the settings.ini and try again. If nothing else works delete the settings.ini file and reload script.")
        is_first_start = bool(int(default_settings["is_first_start"]))
        username = default_settings["username"]
        difficulty = default_settings["difficulty"]
        max_tries = default_settings["max_tries"]
        wordlist = default_settings["wordlist_path"] + default_settings["wordlist_filename"]

# Update the values of the settings in settings.ini
def update_settings() -> None:
    try:
        config["MAIN"]["is_first_start"] = str(int(is_first_start))
        config["MAIN"]["username"] = username
        config["MAIN"]["difficulty"] = str(difficulty)
        config["MAIN"]["max_tries"] = str(max_tries)
        config["MAIN"]["wordlist_path"] = os.path.split(wordlist)[0]
        config["MAIN"]["wordlist_filename"] = os.path.split(wordlist)[1]
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
    pass

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
        print("--Welcome to the hangman console game!--")
        print("Created by: Noel Nagy")
        print("\nWe see that you are new to this game(or reseted the settings)! Please enter your name to get started!\n")
        inp = ""
        while inp == "" or inp == " ":
            try:
                inp = input("My name is: ")
                if inp == "" or inp == " ":
                    raise Exception()
            except:
                print("Your name can't be blank!\n")
        username = inp
        is_first_start = False
        print(f"\nHey {username}! If you enjoy the game please leave a revive on my github page! Have fun! https://github.com/nagynooel/Hangman\n")
        update_settings()

    # This is the main loop for the game. If this ends the script will stop running.
    while True:
        print("--Welcome to the hangman console game!--")
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