# Author: Fernando Saraiva
"""Country Quiz - entry point. Only function calls and their processing."""
from api import lookup_country
from menu import color, show_menu, user_input
from quiz import play_quiz
from storage import load_countries, save_result, show_log


def add_note():
    """Ask for a short note and append it to the log file."""
    note = user_input("Your note: ")
    save_result(f"Note: {note}")
    print(color("Saved!", "green"))


def main():
    """Run the interactive menu loop until the user types 'exit'."""
    countries = load_countries()
    while True:
        show_menu()
        choice = user_input("\nChoose: ", ["1", "2", "3", "4", "exit"])
        if choice == "1":
            play_quiz(countries)
        elif choice == "2":
            lookup_country()
        elif choice == "3":
            show_log()
        elif choice == "4":
            add_note()
        else:
            print(color("Goodbye! 👋", "magenta"))
            break


if __name__ == "__main__":
    main()
