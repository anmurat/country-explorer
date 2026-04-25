import requests
import sys

def get_country(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"❌ '{name}' not found. Check the spelling and try again.")
        return
    elif response.status_code != 200:
        print(f"❌ Something went wrong. Status code: {response.status_code}")
        return

    data = response.json()[0]

    country_name = data["name"]["common"]
    capital = data.get("capital", ["N/A"])[0]
    population = data["population"]
    region = data["region"]
    flag = data.get("flag", "")
    currencies = data.get("currencies", {})
    currency = list(currencies.values())[0]["name"] if currencies else "N/A"
    languages = data.get("languages", {})
    language = ", ".join(languages.values()) if languages else "N/A"

    print(f"\n{flag} {country_name}")
    print(f"   Capital    : {capital}")
    print(f"   Population : {population:,}")
    print(f"   Region     : {region}")
    print(f"   Currency   : {currency}")
    print(f"   Language(s): {language}")
    print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <country> [country2] [country3] ...")
        print("Example: python main.py turkey germany japan")
        return

    countries = sys.argv[1:]

    for country in countries:
        get_country(country)

if __name__ == "__main__":
    main()