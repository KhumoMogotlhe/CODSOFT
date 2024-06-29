import unittest
from unittest.mock import patch
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

class TestRockPaperScissors(unittest.TestCase):

    def test_get_computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        for _ in range(100):  # Run multiple times to ensure randomness
            self.assertIn(get_computer_choice(), choices)

    def test_determine_winner_tie(self):
        self.assertEqual(determine_winner('rock', 'rock'), 'tie')
        self.assertEqual(determine_winner('paper', 'paper'), 'tie')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'tie')

    def test_determine_winner_user(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'user')
        self.assertEqual(determine_winner('paper', 'rock'), 'user')
        self.assertEqual(determine_winner('scissors', 'paper'), 'user')

    def test_determine_winner_computer(self):
        self.assertEqual(determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(determine_winner('rock', 'paper'), 'computer')
        self.assertEqual(determine_winner('paper', 'scissors'), 'computer')

    @patch('builtins.input', side_effect=['rock', 'no'])
    @patch('random.choice', return_value='scissors')
    def test_play_round_user_wins(self, mock_random_choice, mock_input):
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        from main import play_round, main
        result = play_round()

        sys.stdout = sys.__stdout__

        self.assertEqual(result, 'user')
        self.assertIn("The computer chose: scissors", captured_output.getvalue())
        self.assertIn("You win!", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
