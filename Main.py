import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    number_chars = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special_chars else ""

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars

    # Check if user specified preferences result in a valid password
    if len(all_chars) == 0:
        return "Invalid password preferences"

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# User input
length = int(input("Enter the desired password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
use_special_chars = input("Include special characters? (y/n): ").strip().lower() == "y"

# Generate and print the password
password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
print("Generated Password: ", password)