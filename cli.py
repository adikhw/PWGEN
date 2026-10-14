from generator import generate_password
from validator import assess_password


def ask_int(prompt, low, high):
    """Prompt for an integer within the specified range."""
    while True:
        text = input(prompt)
        if not text:
            print("Input cannot be empty")
            continue

        try:
            number = int(text)
        except ValueError:
            print("Input must be a number")
            continue

        if number < low or number > high:
            print(f"Number must be between {low} and {high}")
            continue

        return number


def ask_yes_no(prompt):
    """Prompt the user for a yes-or-no answer."""
    while True:
        answer = input(prompt + " (y/n): ").lower().strip()

        if answer == "y":
            return True
        if answer == "n":
            return False

        print("Answer with y or n")


def generate_menu():
    """Collect options and generate a password."""
    length = ask_int("Length: ", 8, 64)

    use_lower = ask_yes_no("Use lowercase letters?")
    use_upper = ask_yes_no("Use uppercase letters?")
    use_digit = ask_yes_no("Use digits?")
    use_symbol = ask_yes_no("Use symbols?")

    try:
        password = generate_password(length, use_lower, use_upper, use_digit, use_symbol)
        print(password)
    except ValueError as e:
        print(e)


def validate_menu():
    """Check password strength and display the assessment."""
    password = input("Password: ")

    try:
        result = assess_password(password)
        print(f"Level: {result['level']}")

        for reason in result["reasons"]:
            print("- " + reason)
    except ValueError:
        print("Password cannot be empty")


def show_menu_and_run():
    """Display the main menu and handle user choices."""
    while True:
        print("1. Generate password")
        print("2. Check password strength")
        print("3. Exit")
        choice = ask_int("Choose: ", 1, 3)

        if choice == 1:
            generate_menu()
        elif choice == 2:
            validate_menu()
        else:
            print("Goodbye")
            return