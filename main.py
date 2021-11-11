# package: Hangman
# Created by: Noel Nagy
# Website: https://github.com/nagynooel

# -- Functions
# Read settings file if exsists, otherwise create default config file.
def get_settings() -> None:
    pass

def update_settings() -> None:
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
    main_menu_page()