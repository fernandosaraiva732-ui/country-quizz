"""Quiz logic: pick random countries and check the player's answers."""
import random
import time

from api import get_capital
from menu import color, slow_print, user_input
from storage import save_result

QUESTIONS_PER_ROUND = 5


def pick_country(countries, used):
    """Return a random country not in the `used` set, and add it to the set.

    Returns None when every country has been used.
    """
    available = [c for c in countries if c not in used]
    if not available:
        return None
    country = random.choice(available)
    used.add(country)
    return country


def get_question(countries, used):
    """Return a tuple (country, capital) for a country the API knows.

    Countries the API cannot answer are skipped (up to 10 tries).
    """
    for _ in range(10):
        country = pick_country(countries, used)
        if country is None:
            return None
        capital = get_capital(country)
        if capital:
            return (country, capital)
    return None


def check_answer(answer, capital):
    """Return True if the answer matches the capital (ignoring case/spaces)."""
    return answer.strip().lower() == capital.strip().lower()


def ask_question(number, question):
    """Ask one question, print feedback, and return True if correct."""
    country, capital = question
    print()
    answer = user_input(f"Q{number}. What is the capital of {color(country, 'yellow')}? ")
    if check_answer(answer, capital):
        slow_print(color("Correct! ✅", "green"))
        return True
    slow_print(color(f"Wrong ❌ The answer is {capital}.", "red"))
    return False


def play_quiz(countries):
    """Play one round of the quiz and save the score to the log file."""
    if not countries:
        print(color("No countries loaded. Check countries.txt!", "red"))
        return
    used = set()
    score = 0
    asked = 0
    slow_print("Let's play! Fetching questions from the API...")
    for number in range(1, QUESTIONS_PER_ROUND + 1):
        question = get_question(countries, used)
        if question is None:
            print(color("Could not get a question (check your internet).", "red"))
            break
        asked += 1
        if ask_question(number, question):
            score += 1
        time.sleep(0.5)
    if asked:
        print(f"\nYour score: {color(f'{score}/{asked}', 'cyan')}")
        save_result(f"Quiz score: {score}/{asked}")
