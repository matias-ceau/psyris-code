#!/usr/bin/bash

# Define the search query
QUERY="(\"Hallucinogens/adverse effects\"[Mesh] OR \"Hallucinogens/poisoning\"[Mesh] OR \"Hallucinogens/toxicity\"[Mesh]) AND (English[lang] OR French[lang]) AND \"Case Reports\"[Publication Type]"

# Count total number of results
TOTAL_COUNT=$(esearch -db pubmed -query "$QUERY" | xtract -pattern ENTREZ_DIRECT -element Count)

echo "Total number of results: $TOTAL_COUNT"

# Retrieve all results
esearch -db pubmed -query "$QUERY" | \
    efetch -format ris > hallucinogens_case_reports_all.ris

echo "All $TOTAL_COUNT results have been saved to hallucinogens_case_reports_all.ris"
