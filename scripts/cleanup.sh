#!/usr/bin/env bash

RECORDS='tmp'

if [[ -n "$1" ]]; then
    RECORDS="$1"
fi

echo "Type 'yes' to continue..."
read p
if [[ 'yes' != "$p" ]]; then
    exit
fi

echo "Removing from $RECORDS..."

for r in "$RECORDS"/*.wav; do
    name="$(cut  -f1 -d . <<< $r)"
    if [[ ! -f "$name.txt" ]]; then
        echo $name
        rm "$name.wav"
    fi
done