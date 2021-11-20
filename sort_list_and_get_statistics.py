# package: Hangman
# Created by: Noel Nagy
# Website: https://github.com/nagynooel

# Sort list from file by lenght
def sort_by_length(filename: str) -> bool:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    # Place a new line operator to the last word in the file if it doesn't have one, soo it wont melt with another word after sorting.
    if "\n" not in lines[len(lines)-1]:
        lines[len(lines)-1] = lines[len(lines)-1] + "\n"
    try:
        file = open(filename, "w")
        sorted_lines = sorted(lines, key=len)
        file.write("".join(sorted_lines))
        file.close()
    except Exception as e:
        file = open(filename, "w")
        file.write(lines)
        file.close()
        print("List sorting error: Something went wrong, list was successfully reverted to old list!")
        print(e)
        exit()
    return True

# Give average, minimum and maximum length of words in file
def statistics(filename: str) -> None:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    sumOfLen: float = 0.0
    for num in lines:
        sumOfLen += len(num) - 1
    average_length: float = sumOfLen/len(lines)
    min_length: int = len(lines[0])
    max_length: int = len(lines[len(lines)-1])
    print("\nNumber of words:", len(lines))
    print("Average word length:", str(round(average_length, 2)))
    print("Minimum word length:", str(min_length-1))
    print("Maximum word length:", str(max_length-1))

# Menu for the script
if __name__ == "__main__":
    filename = "wordlist.txt"
    print("Select operation:")
    print("1 Sort by length")
    print("2 Statistics (relies on a sorted file)")
    print("3 Both of them")
    operation: int = int(input("Operation: "))
    if operation == 1:
        if sort_by_length(filename):
            print("\nSorting by length is successful!")
    elif operation == 2:
        statistics(filename)
    elif operation == 3:
        if sort_by_length(filename):
            print("\nSorting by length is successful!")
        statistics(filename)