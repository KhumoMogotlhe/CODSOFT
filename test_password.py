import unittest
import string
import random

def generate_password(length):
    if length < 10:
        raise ValueError("Password length should be at least 10 characters to include one of each required type.")
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    if length > 4:
        all_characters = uppercase + lowercase + digits + special
        password.extend(random.choice(all_characters) for _ in range(length - 4))

    random.shuffle(password)

    return ''.join(password)

class TestPasswordGenerator(unittest.TestCase):

    def test_password_length_too_short(self):
        with self.assertRaises(ValueError):
            generate_password(9)

    def test_password_correct_length(self):
        for length in range(10, 20):
            password = generate_password(length)
            self.assertEqual(len(password), length)

    def test_password_contains_required_characters(self):
        password = generate_password(12)
        self.assertTrue(any(c in string.ascii_uppercase for c in password), "Password should contain at least one uppercase letter")
        self.assertTrue(any(c in string.ascii_lowercase for c in password), "Password should contain at least one lowercase letter")
        self.assertTrue(any(c in string.digits for c in password), "Password should contain at least one digit")
        self.assertTrue(any(c in string.punctuation for c in password), "Password should contain at least one special character")

if __name__ == "__main__":
    unittest.main()
