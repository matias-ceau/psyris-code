#!/usr/bin/bash

esearch -db pubmed -query "(\"Hallucinogens/adverse effects\"[Mesh] OR \"Hallucinogens/poisoning\"[Mesh] OR \"Hallucinogens/toxicity\"[Mesh]) AND (\"2000\"[PDAT] : \"2024\"[PDAT]) AND (English[lang] OR French[lang]) AND (\"Systematic Review\"[ptyp])" |
efetch -format ris
