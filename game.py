import random

print("Welcome to the Rock 🪨 Paper📰 Scissors✂️ game!")
user = input("Dear user, please enter your name to start the game: ")
print(f"Hello, Mr. {user}! Thank you for playing the game.")

entry = input("Please enter what you want to take: rock, paper, or scissors: ")
user_choice = entry.lower()  # Convert user input to lowercase for easy comparison

computer_choices = ["rock", "paper", "scissors"]
computer_select = random.choice(computer_choices)
print(f"Computer's choice: {computer_select}")

# Check who wins
if user_choice == computer_select:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_select == "paper":
        print(f"User {user} wins!")
    else:
        print(f"User {user} wins!")
elif user_choice == "paper":
    if computer_select == "scissors":
        print("Computer wins!")
    else:
        print(f"User {user} wins!")
elif user_choice == "scissors":
    if computer_select == "rock":
        print("Computer wins!")
    else:
        print(f"User {user} wins!")
else:
    print("Invalid input. Please enter either 'rock', 'paper', or 'scissors'.")
