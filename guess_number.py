# guess_number.py

def main():
    print("Welcome to the Guess the Number Game!")
    correct_number = 13
    guess_count = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            guess_count += 1

            if 1 <= guess <= 20:
                if guess < correct_number:
                    print("Higher")
                elif guess > correct_number:
                    print("Lower")
                else:
                    print(f"Congratulations! You've guessed the correct number {correct_number} in {guess_count} guesses.")
                    break
            else:
                print("Error: Please guess a number between 1 and 20.")
        
        except ValueError:
            print("Error: Invalid input. Please enter an integer between 1 and 20.")

if __name__ == "__main__":
    main()
