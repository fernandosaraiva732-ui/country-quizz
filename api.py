"""REST Countries API: fetch and display information about a country."""
import requests

from menu import color, user_input
from storage import save_result

BASE_URL = "https://restcountries.com/v3.1/name/"
FIELDS = "name,capital,region,population,languages,currencies"


def _request(name, full_text):
    """Send one request to the API and return the parsed JSON or None."""
    params = {"fields": FIELDS, "fullText": str(full_text).lower()}
    try:
        response = requests.get(BASE_URL + name, params=params, timeout=5)
    except requests.RequestException:
        return None
    if response.status_code != 200:
        return None
    return response.json()


def get_country_info(name):
    """Return a dict with info about `name`, or None if not found.

    Tries an exact match first, then a partial match.
    """
    data = _request(name, True) or _request(name, False)
    if not data:
        return None
    for entry in data:
        if entry["name"]["common"].lower() == name.lower():
            return entry
    return data[0]


def get_capital(name):
    """Return the capital of `name` as a string, or None if unavailable."""
    info = get_country_info(name)
    if not info or not info.get("capital"):
        return None
    return info["capital"][0]


def show_country(info):
    """Print the details of a country dictionary neatly."""
    languages = ", ".join(info.get("languages", {}).values()) or "n/a"
    currencies = ", ".join(c["name"] for c in info.get("currencies", {}).values()) or "n/a"
    capital = ", ".join(info.get("capital", [])) or "n/a"
    print()
    print(color(info["name"]["common"], "yellow"))
    print(f"  Capital:    {capital}")
    print(f"  Region:     {info.get('region', 'n/a')}")
    print(f"  Population: {info.get('population', 0):,}")
    print(f"  Languages:  {languages}")
    print(f"  Currencies: {currencies}")


def lookup_country():
    """Ask for a country name, fetch it from the API and display it."""
    name = user_input("Country name: ")
    print("Searching...")
    info = get_country_info(name)
    if info is None:
        print(color("Country not found (or no internet connection).", "red"))
        return
    show_country(info)
    save_result(f"Lookup: {info['name']['common']}")
