# Country Quiz

**Authors:** Fernando Saraiva

## Description
A terminal app that tests your geography knowledge. It loads countries from
`countries.txt`, asks you for their capitals (data from the REST Countries API),
lets you look up any country, and keeps a log of your results.

## Purpose
Helps you learn world capitals and quickly look up facts about countries.

## How to run
```
pip install -r requirements.txt
python main.py
```
Keep `countries.txt` in the same folder as `main.py`. An internet connection is needed for the quiz and lookup.

## Project structure
| File | Contents |
|------|----------|
| `main.py` | menu loop and function calls only |
| `menu.py` | menu, coloured/delayed output, `user_input` |
| `quiz.py` | quiz logic |
| `api.py` | REST Countries API requests |
| `storage.py` | reading `countries.txt`, writing/reading `results.txt` |

## Points I accomplished and want to be graded for
- **Menu:** interactive menu, returns after each action, exits only with `exit`
- **Menu design (🌶️):** coloured text, typing effect, emojis, delayed output
- **Decomposition:** all functions except `main` live in separate files; no file has more than 10 functions or 300 lines; no code outside functions
- **External file:** reads `countries.txt`
- **Log file (🌶️):** `save_result()` sends new data to `results.txt`, `show_log()` displays it
- **API:** REST Countries API in `api.py`
- **Data structures:** list (countries), set (used countries), tuple (country, capital), dict (API data)
- **Validation:** `user_input()` handles and validates all user input
- **Documentation:** docstrings for every function
- **README.md and requirements.txt**
- **Atomic git commits (🌶️)**
- **Early submission (🌶️)**

## TODO
- Difficulty levels
- High-score table
