import random
import string


def generate_password(
    length: str, include_punctuation: bool, include_digits: bool
) -> str:
    if not length.isdigit():
        raise ValueError("Length must be a positive integer.")

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    return "".join(random.SystemRandom().choice(characters) for _ in range(int(length)))


def get_yes_no_input(prompt: str) -> bool:
    while True:
        response = input(prompt).strip().upper()
        if response == "Y" or response == "y" or response == "":
            return True
        elif response == "N" or response == "n":
            return False
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")


try:
    length = input("Password length: ")
    include_punctuation = get_yes_no_input("Include punctuation characters? (y/N): ")
    include_digits = get_yes_no_input("Include digits? (y/N): ")

    password = generate_password(length, include_punctuation, include_digits)
    print(password)
except ValueError as err:
    print(err)
