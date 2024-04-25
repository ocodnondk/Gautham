import random

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("User Score:", user_score, "Computer Score:", computer_score)
        print("Enter your choice (rock, paper, scissors): ")
        user = input().lower()

        while user not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Enter your choice (rock, paper, scissors): ")
            user = input().lower()

        computer = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chose:", computer)

        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print("Do you want to play again? (yes/no): ")
        play_again = input().lower()

        if play_again != 'yes':
            break

play_game()
