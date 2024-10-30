#!/usr/bin/python

import json
import sys

import matplotlib.pyplot as plt
import requests

if len(sys.argv) == 2:
    if sys.argv[1].lower() in "french":
        CORPUS, LANG = "fr", "French"
        TERMS = [
            "psychédélique_INF",
            "LSD",
            "hallucinog_INF",
            "psilocybine",
            "mescaline",
            "2C-B",
        ]
else:
    CORPUS, LANG = "en_us", "American English"
    TERMS = [
        "psychedelic_INF",
        "LSD",
        "hallucinog_INF",
        "psilocybin",
        "mescaline",
        "2C-B",
    ]


def get_ngram_data(start_year, end_year):
    base_url = "https://books.google.com/ngrams/json"
    params = {
        "content": ",".join(TERMS),
        "year_start": start_year,
        "year_end": end_year,
        "corpus": CORPUS,
        "smoothing": 3,
    }
    response = requests.get(base_url, params=params)
    return response.json()


def plot_ngram_data(data):
    plt.figure(figsize=(12, 6))

    print(json.dumps(data, indent=2))

    for T, term_data in zip(TERMS, data):
        if "timeseries" in term_data:
            years = range(
                term_data.get("firstYear", start_year),
                term_data.get("lastYear", end_year) + 1,
            )
            values = term_data["timeseries"]
            plt.plot(years, values, label=term_data.get("ngram", ""))
        else:
            print(f"No data for {T}")

    plt.title("Frequency of mentions in the english corpus")
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.show()


start_year = 1938
end_year = 2019

# Obtention et affichage des données
ngram_data = get_ngram_data(start_year, end_year)
plot_ngram_data(ngram_data)
