import random

print("\n\n\n\n----Welcome to the Hangman!!----")
menu=True
while menu==True:
    start = input("\nType \"tut\" for tutorial!\nPress enter if you are ready to play!! ")
    restart=False
    if start=="quit":
        print("\nThank you for playing!","--------")
        exit()
    if start=="tut":
        print("Welcome to the tutorial!!\nI am sorry but we are currently working on this page!")
        input("Please press enter to go back to the startmenu! ")
    if start=="":
        restart=True
        menu=False
while restart==True:
    f = open("wordlist.txt", "r")
    nouns=f.readlines()
    noun = nouns[random.randint(0,len(nouns))]
    f.close()

    print("\n\nThe world has been selected! Good luck!\n\n")
    n=0
    for x in noun:
        n+=1
        if n==len(noun):
            continue
        print("_",end=" ")
    guessed = []
    z=0
    for x in noun:
        z+=1
        if z!=len(noun):
            guessed.append(".")
    count = 0
    run = True
    while run==True:
        letter = input("\n\nType a letter: ")
        if letter == 'quit':
            print("\nThank you for playing!","--------")
            exit()
        if len(letter) > 1:
            print("Please type only one letter")
            continue
        if letter in noun:
            i=0
            for x in noun:
                i+=1
                if i==len(noun):
                    continue
                if i != len(noun)-1:
                    if x==letter:
                        print(letter,end=" ")
                        guessed[i-1] = letter
                    else:
                        if guessed[i-1] == ".":
                            print("_",end=" ")
                        else:
                            print(guessed[i-1], end=" ")
                else:
                    if x==letter:
                        print(letter)
                        guessed[i-1] = letter
                    else:
                        if guessed[i-1] == ".":
                            print("_")
                        else:
                            print(guessed[i-1])
        else:
            print("\nThe word doesn't contain the letter:",letter)
            count+=1
            y=0
            for x in noun:
                y+=1
                if y==len(noun):
                    continue
                if y!=len(noun):
                    if guessed[y-1] != ".":
                        print(x,end=" ")
                    else:
                        print("_",end=" ")
                else:
                    if guessed[y-1] != ".":
                        print(x)
                    else:
                        print("_")
        if "." not in guessed:
            print("\nCongratulations you won!!")
            run=False
            over = input("Do you wanna start over? y/n ")
            if over=="n":
                print("\nThank you for playing!","--------")
                restart=False
        if count==6:
            print("\nYou lost!")
            print("The word was: ",end=" ")
            for x in noun:
                print(x, end=" ")
            run=False
            over = input("\nDo you wanna start over? y/n ")
            if over=="n":
                print("\nThank you for playing!","--------")
                restart=False
