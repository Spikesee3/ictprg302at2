import os
import random
repeatplay = 1

while repeatplay != 0:
    print("--------------------------------------\n| __      __   _                  _  |\n| \\ \\    / /__| |__ ___ _ __  ___| | |\n|  \\ \\/\\/ / -_) / _/ _ \\ '  \\/ -_)_| |\n|   \\_/\\_/\\___|_\\__\\___/_|_|_\\___(_) |\n--------------------------------------\n")
    print(f"The current highscore is: {str(open('highscore.txt').read())} made by {str(open('highscorename.txt').read())}")
    name = input("What's your name?: ")
    repeatplay = 1
    def numberguess():
        attempts = 0
        number = random.randint(1, 100)
        guess = int(input("Guess a number from 1-100: "))
        while True:
            if guess > number:
                guess = int(input("The number is lower, guess again: "))
                attempts = attempts + 1
            elif guess < number:
                guess = int(input("The number is higher, guess again: "))
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
                        break
                    else:
                        print("You chose not to save your highscore")
                        break
                elif highscore < attempts:
                    print(f"You did not get a highscore, the current highscore is {highscore}") # i forgot what the syntax was for smaller or equal to so i did it twice i know it's ass
                    break
                elif highscore == attempts:
                    print(f"You did not get a highscore, the current highscore is {highscore}")
                    break
            else:
                print(f"{guess} is not a valid number, please choose a number from 1-100")
    numberguess()             
                    
    def repeatplay():
            playagain = input("Play again? (y/n): ")
            if playagain == "y":
                repeatplay = 0
            elif playagain == "n":
                print("Thanks for playing!")
                exit()
    repeatplay()