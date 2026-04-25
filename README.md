# 🌍 Country Explorer

A simple Python CLI tool that fetches real-time country data using the [REST Countries API](https://restcountries.com/).

## Features

- Search any country by name
- Compare multiple countries at once
- Displays capital, population, region, currency and language(s)
- Handles errors gracefully

## Requirements

- Python 3.x
- `requests` library

## Installation

git clone https://github.com/anmurat/country-explorer.git
cd country-explorer
pip install requests

## Usage

Single country:
python main.py turkey

Multiple countries:
python main.py turkey germany japan

## Example Output

🇹🇷 Turkey
   Capital    : Ankara
   Population : 85,664,944
   Region     : Asia
   Currency   : Turkish lira
   Language(s): Turkish

🇩🇪 Germany
   Capital    : Berlin
   Population : 83,491,249
   Region     : Europe
   Currency   : euro
   Language(s): German

## API

Data provided by REST Countries (https://restcountries.com) — free, no API key required.
