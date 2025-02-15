"""This file is used to convert the Psychedelics.csv file into JSON format."""

import json
from pathlib import Path
import pandas as pd
import re
from ..utils import Utils


class CSVToJSON:
    """A class to convert CSV files to JSON format with optional cleaning features.

    This class provides functionality to read CSV files, convert them to JSON format,
    and apply various cleaning operations on the data. It can handle numbered lists
    and specific date formats, particularly suited for 'Date_de_debut' fields.

    Attributes:
        path (Path): Path to the input CSV file.
        df (pandas.DataFrame): DataFrame containing the CSV data.
        json (list): List of dictionaries containing the raw JSON conversion.
        cleaned_json (list): List of dictionaries containing the cleaned JSON conversion.
        documents (None): Reserved for future use.

    Methods:
        _read_csv(): Reads and initializes the CSV data.
        _clean_numbered_list(value): Cleans numbered list strings into actual lists.
        _clean_date_de_debut(value): Extracts and formats dates from strings.
        convert_csv_to_json(): Converts CSV data to raw JSON format.
        convert_csv_to_cleaned_json(): Converts CSV data to cleaned JSON format.
        save_json(output_path, cleaned=False): Saves JSON data to a file.
        explore_csv(): Prints exploratory analysis of the CSV structure.

    Example:
        converter = CSVToJSON(Path('data.csv'))
        converter.save_json('output.json', cleaned=True)
    """

    def __init__(self, path: Path):  # Changed default model
        self.path = path
        self.df = self._read_csv()
        self.json = self.convert_csv_to_json()
        self.cleaned_json = self.convert_csv_to_cleaned_json()
        self.documents = None
        # Exploratory pass: print CSV overview
        print("CSV columns:", self.df.columns.tolist())
        print("CSV preview:", self.df.head())

    def _read_csv(self):
        df = pd.read_csv(self.path, sep=",", encoding="utf-8")
        df.columns = [Utils.clean_variable_name(col) for col in df.columns]
        return df

    def _clean_numbered_list(self, value):
        if not isinstance(value, str):
            return value

        # Split on numbered items (e.g. "1. Item1 2. Item2")
        items = re.split(r"(?=\d+\.)", value.strip())
        # Remove empty strings and clean each item
        items = [item.strip() for item in items if item.strip()]

        # If no numbered items found, return original value
        if not items or not all(re.match(r"\d+\.", item) for item in items):
            return value

        # Remove numbers and clean items
        cleaned_items = [re.sub(r"^\d+\.\s*", "", item).strip() for item in items]
        cleaned_items = [i for i in cleaned_items if i != ""]
        return cleaned_items

    def _clean_date_de_debut(self, value):
        if not isinstance(value, str):
            return []
        # Use re.findall to extract all date patterns (allowing optional whitespace)
        matches = re.findall(r"(\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})", value)
        return matches

    def convert_csv_to_json(self):
        documents = []
        for _, row in self.df.iterrows():
            doc = {row.name: row.to_dict()}
            documents.append(doc)
        return documents

    def convert_csv_to_cleaned_json(self):
        documents = []
        for _, row in self.df.iterrows():
            cleaned_row = {}
            for key, value in row.items():
                if key == "Date_de_debut":
                    cleaned_row[key] = self._clean_date_de_debut(value)
                else:
                    cleaned_row[key] = self._clean_numbered_list(value)
            doc = {row.name: cleaned_row}
            documents.append(doc)
        return documents

    def save_json(self, output_path, cleaned=False):
        data = self.cleaned_json if cleaned else self.json
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # New: Add an exploratory method to inspect CSV structure
    def explore_csv(self):
        print("Exploratory Analysis:")
        print("Columns:", self.df.columns.tolist())
        for col in self.df.columns:
            print(f"{col} (sample values): {self.df[col].dropna().unique()[:5]}")
