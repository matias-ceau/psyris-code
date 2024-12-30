#!/usr/bin/bash

export _START='## CLASSIFICATION'
export _END='## VOIE D.ADMINISTRATION'
export _STRING='^lu: false$'
export _FOLDER="$PSYRIS/NOTES/CASES/nots_21_24/"
export _SUBSTITUTION='s#(^[0-9]*\.) (.*)$#\1 \2@\1 \[\2](<NOTES/CASES/generated_substance/\2.md>)#'
export _INCLUDE_STRING='[0-9]*\. [^\[]*'
export _EXCLUDE_STRING='[\[\]]'

search_cmd() {
    rg "$_STRING" "$_FOLDER" --files-with-matches
}

show_substance() {
    first=$(rg --line-number "$_START" "$1" | cut -d: -f1)
    last=$(rg --line-number "$_END" "$1" | cut -d: -f1)
    bat -r "${first}:${last}" "$1"
}
export -f show_substance

preview_substitution() {
    content="$(show_substance "$1" | rg "$_INCLUDE_STRING" | sed -E "$_SUBSTITUTION")"
    echo -e "$content" | while read -r line; do
        origin="$(cut -d@ -f1 <<< "$line")"
        output="$(cut -d@ -f2 <<< "$line")"
        echo -e "\e[9;31m${origin}\e[0m\t\e[32m${output}\e[0m"
    done
}
export -f preview_substitution

search_cmd |
fzf \
    --ansi \
    --preview 'preview_substitution {}' \
    --preview-window 'top,80%' \
    --with-nth -1 \
    --delimiter '/' \
    --bind 'enter:become(show_substance {})'

