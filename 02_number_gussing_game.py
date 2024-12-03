import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter a number Between 1  and 100: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print("Well Done! You are Win")
            break
    except ValueError:
        print("Please Enter a valid number")