#!/usr/bin/env bash

ROOT="$1"
METADATA="./metadata.csv"

echo -n "" > $METADATA

for i in $(ls -1 "$ROOT"/*.txt); do
    id=$(basename $i | cut -d . -f1)

    echo "$id|$(cat $i)" >> $METADATA

    if [[ $2 = "delete-txt" ]]; then
        echo Deleting txt file:  $i
        rm "$i"
    fi
done


