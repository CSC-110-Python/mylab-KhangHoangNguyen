# test_scores.py

def main():
    print("Welcome to the Test Scores Program")
    
    total_score = 0
    count = 0

    while True:
        try:
            score = int(input("Enter a test score (or 999 to finish): "))

            if score == 999:
                break

            if 0 <= score <= 100:
                total_score += score
                count += 1
            else:
                print("Error: Test score must be between 0 and 100. Please try again.")
        
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

    if count > 0:
        average_score = total_score / count
        print(f"\nTotal score: {total_score}")
        print(f"Average score: {average_score:.2f}")
    else:
        print("\nNo valid test scores were entered.")

if __name__ == "__main__":
    main()
