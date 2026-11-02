
print("Number Guessing Intelligent Agent")
print("Think of a number between 1 and 100.")

low = 1
high = 100
attempts = 0

while low <= high:

    guess = (low + high) // 2
    attempts += 1

    print("\nMy guess is:", guess)

    feedback = input("Enter higher, lower or correct: ").lower()

    if feedback == "higher":
        low = guess + 1

    elif feedback == "lower":
        high = guess - 1

    elif feedback == "correct":
        print("I guessed your number!")
        print("Total attempts:", attempts)
        break

    else:
        print("Invalid feedback! Try again.")

if low > high:
    print("Your feedback was incorrect!")

