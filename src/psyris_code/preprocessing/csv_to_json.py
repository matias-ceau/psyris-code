import json
from rdflib import Graph, Namespace
from jsonschema import validate
from pathlib import Path
import pandas as pd
from ..utils import Utils


class CSVToJSON:

    def __init__(self, path: Path):
        self.path = path
        self.df = self._read_csv()
        self.json = self.convert_csv_to_json()

    def _read_csv(self):
        df = pd.read_csv(self.path, sep=",", encoding="utf-8")
        df.columns = [Utils.clean_variable_name(col) for col in df.columns]
        return df

    def convert_csv_to_json(self):
        documents = []
        for _, row in self.df.iterrows():
            doc = {row.name: row.to_dict()}
            documents.append(doc)
        return documents
