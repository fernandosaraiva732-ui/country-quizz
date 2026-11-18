"""File handling: load countries, write to and read from the log file."""
import os
import re
from datetime import datetime

COUNTRIES_FILE = "countries.txt"
LOG_FILE = "results.txt"


def clean_name(line):
    """Remove text in {braces} and extra punctuation from a country line."""
    name = re.sub(r"\{.*?\}", "", line)
    return name.strip().strip(",").strip()


def load_countries(path=COUNTRIES_FILE):
    """Read countries.txt and return a list of cleaned country names.

    Returns an empty list if the file is missing.
    """
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        names = [clean_name(line) for line in f]
    return [n for n in names if n]


def save_result(text, path=LOG_FILE):
    """Append a timestamped line to the log file."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{stamp}] {text}\n")


def show_log(path=LOG_FILE):
    """Print the whole contents of the log file."""
    if not os.path.exists(path):
        print("No results saved yet. Play the quiz first!")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    print("\n--- Past results ---")
    print(content if content else "The log is empty.")
