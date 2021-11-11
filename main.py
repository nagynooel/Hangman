# package: Hangman
# Created by: Noel Nagy
# Website: https://github.com/nagynooel

# -- Functions
# Read settings file if exsists, otherwise create default config file.
def get_settings() -> None:
    pass

def update_settings() -> None:
    pass

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
    pass

if __name__ == "__main__":
    main_menu_page()