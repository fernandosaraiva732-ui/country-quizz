"""Menu and input helpers: coloured text, delayed output, validated input."""
import time

RESET = "\033[0m"
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
}


def color(text, name):
    """Return text wrapped in the ANSI colour code for `name`."""
    return f"{COLORS.get(name, '')}{text}{RESET}"


def slow_print(text, delay=0.02):
    """Print text one character at a time for a typing effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def show_menu():
    """Display the main menu."""
    print()
    print(color("=" * 34, "cyan"))
    slow_print(color("     🌍  COUNTRY QUIZ  🌍", "yellow"), 0.01)
    print(color("=" * 34, "cyan"))
    print(color("1", "green") + " - Play quiz (guess the capital)")
    print(color("2", "green") + " - Look up a country (API)")
    print(color("3", "green") + " - View past results")
    print(color("4", "green") + " - Add a note to the log")
    print(color("exit", "red") + " - Quit the program")


def user_input(prompt, valid_options=None):
    """Ask the user for input and validate it.

    If `valid_options` is given, keep asking until the answer (case-insensitive,
    stripped) is one of them. Otherwise, keep asking until it is non-empty.
    Returns the cleaned answer in lowercase only when options are given.
    """
    while True:
        answer = input(prompt).strip()
        if valid_options is None:
            if answer:
                return answer
            print(color("Input cannot be empty.", "red"))
        elif answer.lower() in valid_options:
            return answer.lower()
        else:
            options = ", ".join(valid_options)
            print(color(f"Invalid choice. Options: {options}", "red"))
