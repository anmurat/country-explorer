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

### CLI
Single country:
python main.py turkey

Multiple countries:
python main.py turkey germany japan

### Web Interface
Run the Flask app:
python app.py

Then open your browser and go to:
http://127.0.0.1:5000

## API

Data provided by REST Countries (https://restcountries.com) — free, no API key required.
