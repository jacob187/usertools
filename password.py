import random, string


def generate_password(length: str) -> None:
    if not length.isdigit():
        raise ValueError("Length must be a positive integer.")
    return "".join(
        random.SystemRandom().choice(
            string.ascii_letters + string.digits + string.punctuation
        )
        for _ in range(int(length))
    )


try:
    password = generate_password(input("Password length:"))
    print(password)
except ValueError as err:
    print(err)
