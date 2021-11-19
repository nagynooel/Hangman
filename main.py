# package: Hangman
# Created by: Noel Nagy
# Website: https://github.com/nagynooel

import configparser
import os.path
import random
import webbrowser

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

def reset_settings() -> None:
    pass

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

# Settings pages
# Difficulty levels: Easy - 0 Normal - 1 Hard - 2
# Easy maximum word length: 5
# Normal maximum word length: 10
# Hard maximum word length: no limit
def select_difficulty() -> None:
    global difficulty
    print("\n\n-Select difficulty-")
    print("Type the number of the difficulty!")
    print("1 Easy - maximum word length: 5")
    print("2 Normal - maximum word length: 10")
    print("3 Hard - maximum word length: no limit")
    print("\n4 Back to general settings\n")
    inp = get_menu_user_input(0,4)
    if inp != 4:
        difficulty = inp-1
        update_settings()

# Select the number of maximum tries for a game.
def select_max_tries() -> None:
    global max_tries
    print("\n\n-Select max tries-")
    print("Type in the number of tries you'd like to have to guess the word.")
    print("Minimum number of tries: 1")
    print("Maximum number of tries: 100")
    print(f"Current number of tires: {max_tries}")
    print("\n0 Back to general settings\n")
    inp = get_menu_user_input(0,100)
    if inp != 0:
        max_tries = inp
        update_settings()

def set_new_username() -> None:
    global username
    print("\n\n-Change username-")
    print("Please type in below your new desired username. If you don't want to change your current username please enter the number 0 as an input.")
    print(f"Current username: {username}")
    inp = get_string_user_input("New username: ", False, "Your name can't be blank! Please input a valid username.", [])
    if inp != "0":
        username = inp
        update_settings()

# Modifiy wordlist file
def modify_wordlist() -> None:
    global wordlist
    print("\n\n-Select new wordlist-")
    print("Please input below the filename, esxtension and path of your own wordlist in this format: path/filenam.extension (example: C:\Documents\wordlist.txt)")
    print("Relative paths can also be used. (example: .\wordlist.txt)")
    print("Your wordlist should ideally be a txt file. Other types of files may work too.")
    print("If you'd like to set the wordlist to the default one please input \"reset\".")
    print("If you don't want to change the current list input \"back\"")
    print(f"Current wordlist: {wordlist}")
    # Main loop for input
    does_wordlist_file_exist = False
    while does_wordlist_file_exist == False:
        inp = get_string_user_input("New wordlist: ", False, "Please input a valid wordlist as described above.", [])
        try:
            # Reset wordlist
            if inp == "reset":
                if os.path.isfile(default_settings["wordlist"]):
                    wordlist = default_settings["wordlist"]
                    update_settings()
                    does_wordlist_file_exist = True
                else:
                    # If it doesn't exist throw an error
                    print("The default wordlist CAN NOT be found.")
                    raise Exception()
            # Try to set custom wordlist
            elif inp != "back":
                if os.path.isfile(inp):
                    wordlist = inp
                    update_settings()
                    does_wordlist_file_exist = True
                else:
                    # If it doesn't exist throw an error
                    print("The wordlist, that you entered CAN NOT be found.")
                    raise Exception()
            else:
                does_wordlist_file_exist = True
        except:
            print("Please enter a new wordlist or download the default list from this url: https://github.com/nagynooel/Hangman/blob/master/wordlist.txt")
            # Open the link to download the original wordlist if input is "y"
            inp = get_string_user_input("Would you like to open the above url? (y/n) ", False, "Please enter \"y\" or \"n\" only!", ["y","n"]) 
            if inp == "y":
                webbrowser.open("https://github.com/nagynooel/Hangman/blob/master/wordlist.txt", new=0, autoraise=True)

# Add/Remove word to/from wordlist
def add_word() -> None:
    print("\n\n-Add word into current wordlist-")
    print("Please type in below the new word that you'd like to add to the wordlist. You can enter them one by one or you can even input a list of words seaprated with comas. Example: word1, word2, word3")
    print("If you input (a) word(s) that are already inside the wordlist, it won't add it again.")
    print("Your word can not contain any spaces at this time.")
    print(f"Before you enter the words, please make sure that this is the wordlist you want to append: {wordlist}")
    print("If you do not want to append your wordlist, type \"back\".")
    inp = get_string_user_input("New word(s): ", False, "You can't leave this field blank!", [])
    # Check if input is not "back"
    if inp != "back":
        # Read the file to know if words are in the wordlist already
        with open(wordlist, "r") as file:
            words_in_wordlist: str = file.readlines()
        with open(wordlist, "a") as file:
            new_words: list(str) = inp.replace(" ", "").split(",")
            # This list will ensure that the program won't add the same word twice to the list from one input
            newly_added_words: list(str) = []
            for word in new_words:
                if word + "\n" not in words_in_wordlist and word not in newly_added_words:
                    file.write(word + "\r")
                    newly_added_words.append(word)
                else:
                    print(f"\"{word}\" is already in the wordlist!")

def remove_word() -> None:
    print("\n\n-Remove word from current wordlist-")
    print("Please type in below the word(s) that you'd like to remove from the current wordlist. You can enter them one by one or you can even input a list of words seaprated with comas. Example: word1, word2, word3")
    print("If you input (a) word(s) that do not exist in the wordlist, it will throw an error message.")
    print(f"Before you enter the words, please make sure that this is the wordlist you want to remove from: {wordlist}")
    print("If you do not want to remove words from your wordlist, type \"back\".")
    inp = get_string_user_input("Remove words: ", False, "You can't leave this field blank!", [])
     # Check if input is not "back"
    if inp != "back":
        # Read the wordlist file and get all of the words into a list
        with open(wordlist, "r") as file:
            words_in_wordlist: list(str) = file.readlines()
        # Get the words inputted by the user into a list
        words_to_remove: list(str) = inp.replace(" ", "").split(",")
        # Remove words from the list and if word is not in the file
        for word in words_to_remove:
            if word + "\n" in words_in_wordlist:
                words_in_wordlist.remove(word+"\n")
            elif word in words_in_wordlist:
                words_in_wordlist.remove(word)
            else:
                # Drop and error message
                print(f"\"{word}\" is not in the current wordlist!")
        # Wipe the file clean
        file = open(wordlist, "w")
        file.close()
        # Write the new list of words into the file
        with open(wordlist, "a") as file:
            for word in words_in_wordlist:
                file.write(word)

def settings_page() -> None:
    run_settings_page: bool = True
    while run_settings_page:
        print("\n\n-Settings-")
        print("Type the number of the setting/button, that you'd like to change!")
        print("\nGeneral settings:")
        print("1 Difficulty:", "Easy" if difficulty == 0 else "Normal" if difficulty == 1 else "Hard")
        print(f"2 Number of maximum tries: {max_tries}")
        print(f"3 Username: {username}")
        print("\nWordlist related:")
        print(f"4 Current wordlist: {wordlist}")
        print("5 Add word to wordlist")
        print("6 Remove word from wordlist")
        print("\n7 Reset settings")
        print("\n8 Back to main menu\n")
        inp = get_menu_user_input(1,8)
        # Handle input
        if inp == 1:
            select_difficulty()
        elif inp == 2:
            select_max_tries()
        elif inp == 3:
            set_new_username()
        elif inp == 4:
            modify_wordlist()
        elif inp == 5:
            add_word()
        elif inp == 6:
            remove_word()
        elif inp == 7:
            reset_settings()
        elif inp == 8:
            run_settings_page = False

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