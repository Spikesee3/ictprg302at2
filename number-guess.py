import os
import random
number = random.randint(1, 1000)
attempts = 0
print(f"The current highscore is: {open('highscore.txt').read()}")
guess = int(input("Guess a number from 1-1000: "))
while True:
    number = 111
    if guess > number:
        guess = int(input("Lower "))
        attempts = attempts + 1
    if guess < number:
        guess = int(input("Higher "))
        attempts = attempts + 1
    if guess == number:
        print("Congratulations you guessed the number in " + str(attempts) + " tries!")
        highscore = int(open('highscore.txt').read())
        if highscore > attempts:
            with open('highscore.txt', 'a') as f:
                    
                    f.write(str(attempts) + '\n')
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
            exit