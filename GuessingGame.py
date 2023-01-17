import random

def title():
    print("Guess the number!")
    print()
    print()

def playing(LIMIT):
    number = random.randint(1, LIMIT)
    print(f"Im thinking of a number from 1 to {LIMIT}\n.")
    count = 1
    guess = int(input("Your guess: "))

    while (guess != number):
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        guess = int(input("Your guess: "))
    print(f"You guessed it in {count} tries.\n")

def main():
    title()
    again = "y"
    while again.lower() == "y":
        LIMIT = int(input("Enter the limit: "))
        playing(LIMIT)
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()