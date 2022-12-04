#!/usr/bin/env bash
DIR=data/annotations

echo Arousal
cat $DIR/annotations.arousal.all | grep -v not_selected | python3 scripts/agreement_krippendorff.py

echo Valence
cat $DIR/annotations.valence.all | grep -v not_selected | python3 scripts/agreement_krippendorff.py
