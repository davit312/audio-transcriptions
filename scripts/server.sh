#!/usr/bin/env bash

REC_DIR=tmp

if [[ -n $1 ]]; then
    REC_DIR="$1"
fi

source ~/repos/transcription-maker/.venv/bin/activate
python ~/repos/transcription-maker/app.py "$REC_DIR"
