import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 40)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    use_letters = input("Include letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
