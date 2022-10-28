import random
goal = random.randint(1, 21)
print(f"Try to guess a random number between 1 and 20 in 6 tries!")


for i in range(6):
    guess = int(input("What is your guess? "))
    if guess == goal:
        print(f'Nice! You guessed the number in {i + 1} tries')
        break
    else:
        if i == 5:
            print("Dang, you didn't guess it. The correct number was", goal)
        else:
            if guess > 20:
                print("Bruh. You know what, you don't get to play the game anymore.")
                break
            else:
                if guess > goal:
                    print("Too high. Try again.")
                elif guess < goal:
                    print("Too low. Try again.")
                continue


