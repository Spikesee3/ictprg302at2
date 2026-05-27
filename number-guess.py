import os
import random
while True:
    number = random.randint(1, 1000)
    attempts = 0
    print(f"The current highscore is: {str(open('highscore.txt').read())}")
    guess = int(input("Guess a number from 1-1000: "))
    number = 111 # this is just to skip the game remove in final edits
    if guess == 4: # If you enter 4 it changes the highscore to 99 good for saving time
        with open('highscore.txt', 'a') as f:
                f.truncate(0)
                f.write("99")
                f.close()
        print("Changed the high score to 99")
        continue
    if guess > number:
        guess = int(input("Lower "))
        attempts = attempts + 1
    if guess < number:
        guess = int(input("Higher "))
        attempts = attempts + 1
    if guess == number:
        print("Congratulations you guessed the number in " + str(attempts) + " tries!")
        with open("highscore.txt") as g:
            highscore = float(g.read())
        if highscore > attempts:
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