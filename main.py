import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_round():
    print("Let's play rock, paper and scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    computer_choice = get_computer_choice()
    print(f"The computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

    return winner

def main():
    user_score = 0
    computer_score = 0
    play_again = 'yes'

    while play_again == 'yes':
        winner = play_round()
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes or no): ").lower()
        while play_again not in ['yes', 'no']:
            print("Invalid choice. Please answer 'yes' or 'no'.")
            play_again = input("Do you want to play another round? (yes or no): ").lower()

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
