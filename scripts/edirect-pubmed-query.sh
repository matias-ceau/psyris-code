#!/usr/bin/bash

query='((((("hallucinogens"[All Fields]) OR ("psychedelics"[All Fields]) OR ("hallucinogens"[MeSH Terms]))) AND (("adverse events"[All Fields]) OR ("toxicicity"[All Fields]) OR ("poisoning"[All Fields]) OR ("adverse effects"[All Fields]))) OR ((("hallucinogens/toxicity"[MeSH Terms]) OR ("hallucinogens/poisoning"[MeSH Terms]) OR ("hallucinogens/adverse effects"[MeSH Terms])))) AND (("2000"[Date - Publication] : "2024"[Date - Publication])) AND (("english"[Language]) OR ("french"[Language])) AND ("systematic review"[Publication Type])'

esearch -db pubmed -query "$query" | efetch -format ris > result240924.ris
# "(\
    # \"Hallucinogens/adverse effects\"[Mesh] OR \
    # \"Hallucinogens/poisoning\"[Mesh] OR \
    # \"Hallucinogens/toxicity\"[Mesh]\
    # ) AND \
    # (\"2000\"[PDAT] : \"2024\"[PDAT]) AND \
    # (English[lang] OR French[lang]) AND \
    # (\"Systematic Review\"[ptyp])"
