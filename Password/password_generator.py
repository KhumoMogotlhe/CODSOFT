import random
import string

def generate_password(length):
    if length < 10:
        raise ValueError("Password length should be at least 10 characters to include one of each required type.")
    
    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one of each required character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    # If the length is more than 4, fill the rest with random choices from all characters
    if length > 4:
        all_characters = uppercase + lowercase + digits + special
        password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (at least 10): "))
            if length < 10:
                print("Please enter a number greater than or equal to 10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate the password
    try:
        password = generate_password(length)
    except ValueError as e:
        print(e)
        return

    # Display the generated password
    print("Generated password:", password)

if __name__ == "__main__":
    main()
