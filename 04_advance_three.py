import random

emojis = {'r' : '🐥', 'p': '📰', 's': '✂️' }
choices = ('r', 'p', 's')

def get_user_choice():
    while True:
      user_choice = input("Rock, paper or scissors? (r/p/s): ")
      if user_choice in choices:
        return user_choice
      else:
        print("Invalid Choice!")
    
def displat_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's' ) or 
        (user_choice == 's' and computer_choice == 'p') or 
        (computer_choice == 'p' and user_choice == 'r')):
        print("You Win!")
    else:
        print("You Lose")
        
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        displat_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)
        
        should_continue  = input("Continue? (y/n): ")

        if should_continue == 'n':
            break

play_game()