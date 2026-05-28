import os
import random
while True:
    print("--------------------------------------\n| __      __   _                  _  |\n| \\ \\    / /__| |__ ___ _ __  ___| | |\n|  \\ \\/\\/ / -_) / _/ _ \\ '  \\/ -_)_| |\n|   \\_/\\_/\\___|_\\__\\___/_|_|_\\___(_) |\n--------------------------------------\n")
    name = input("What's your name?: ")
    number = random.randint(1, 100)
    attempts = 0
    print(f"The current highscore is: {str(open('highscore.txt').read())} made by {str(open('highscorename.txt').read())}")
    guess = int(input("Guess a number from 1-100: "))
    if guess == 9999: # If you enter 9999 it changes the highscore to 99 good for saving time
        with open('highscore.txt', 'a') as f:
                f.truncate(0)
                f.write("99")
                f.close()
        print("Changed the high score to 99")
        continue
    elif guess > number:
        guess = int(input("Lower "))
        attempts = attempts + 1
    elif guess < number:
        guess = int(input("Higher "))
        attempts = attempts + 1
    elif guess == number:
        print("Congratulations you guessed the number in " + str(attempts) + " tries!")
        with open("highscore.txt") as g:
            highscore = float(g.read())
        if highscore > attempts:
            if input("Would you like to save your highscore? (y/n): \n") == "y":
                with open('highscorename.txt', 'a') as f:
                        f.truncate(0)
                        f.write(name)
                        f.close() 
                with open('highscore.txt', 'a') as f:
                        f.truncate(0)
                        f.write(str(attempts))
                        f.close()     
        elif highscore < attempts:
            print(f"You did not get a highscore, the current highscore is {highscore}") # i forgot what the syntax was for smaller or equal to so i did it twice i know it's ass
        elif highscore == attempts:
            print(f"You did not get a highscore, the current highscore is {highscore}")
        playagain = input("Play again? (y/n): ")
        if playagain == "y":
            continue
        elif playagain == "n":
            print("Thanks for playing!")
            exit()
    else:
        print(f"{guess} is not a valid number, please choose a number from 1-100")