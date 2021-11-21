# Hangman
Created by: [Noel Nagy](https://github.com/nagynooel "Noel's Github page")

Date of creation: 11.11.2021 - 11.21.2021 (There may be bug fixes after this date!)

Used license: [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html "GNU AGPLv3 License")
## Background of the project
This is an improved version of my previously made console game.

I wrote the previous game when I started experimenting with python. It was about a year ago from the creation of this project! I'd like to see how much I improved since then. I uploaded the old version of the game for reference by the name of "app_old.py".

## Technical data:
Used languages/file types:
* python 3.9.8
   * This is the base language used to program the game. There is also a script included that sorts the wordlist and gives a few statistics back from it.
* txt
   * The wordlist is a txt file which you can edit really easily. I am also planning a feature to the game, where you can add and remove words from the console and change the base list.
* ini
   * There is a settings.ini file included which will hold the most basic settings to the game. I'm planning on using the [configparser](https://docs.python.org/3/library/configparser.html "Configparser documentation") module to edit and read the settings file.

## Scoring system:
The scoring system is based on the selected difficulty. Listed below are the formulas and code implementations used to count them. The code implementation includes one line nested if/else functions for ease of use.
#### Here are the keyes used in the formulas:
* **number of occurences**: The number of times the guessed letter appers in the word. (Example: word: a**pp**le - letter: p - number of occurences: 2)
* **streak**: The users current streak in guessing the word. The streak is by default 0 and is reseted after guessing a letter that is not in the word. After every successfull attempt the streak will be incremented by 1.
### Formulas:
**Easy difficulty (0):**  
gaing points: **number of occurences * streak**  
losing points: - 1  

**Medium difficulty (1):**  
gaing points: **number of occurances * (streak + 1)**  
losing points: - 3

**Hard difficulty (2):**  
gaing points: **number of occurances * (streak + 2)**  
losing points: - 5

### Code implementations:
gaining points:
```python
gain_point_addition: int = 0 if difficulty == 0 else 1 if difficulty == 1 else 2

gained_points: int = number_of_occurrences * (streak + gain_point_addition)
score += gained_points
```
losing points:
```python
lose_points: int = 1 if difficulty == 0 else 3 if difficulty == 1 else 5
score -= lose_points
