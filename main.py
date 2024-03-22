import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation  # character types to be used in password.

    password = ''.join(random.choice(chars) for _ in range(length))    # randomly join charcters.
        
    return password


if __name__ == "__main__":
    password_length = int(input("What length of password do u desire :) "))

    if password_length < 1:
        print("Password length must be at least 1 character.")

    else:
        generated_password = generate_password(password_length)
        print("Generated password:", generated_password)