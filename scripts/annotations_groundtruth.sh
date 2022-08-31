#!/usr/bin/env bash

INDIR=data/annotations
OUTDIR=/tmp
# This OUTDIR will rewrite the dataset files:
# OUTDIR=data/annotations

for TYPE in arousal valence
do
    cat $INDIR/annotations.$TYPE.all | python3 scripts/annotations_agreement.py data/triplets.jsonl > $OUTDIR/annotations.$TYPE.all.agreement
    cat $OUTDIR/annotations.$TYPE.all.agreement | grep -v disagreement | python3 scripts/annotations_triplet_consistency.py > $OUTDIR/annotations.$TYPE.all.agreement.gt
    cat $OUTDIR/annotations.$TYPE.all.agreement.gt | grep \"consistent\" > $OUTDIR/annotations.$TYPE.all.agreement.gt.ct
    cat $OUTDIR/annotations.$TYPE.all.agreement.gt | grep full-agreement > $OUTDIR/annotations.$TYPE.all.agreement.gt.fa
    cat $OUTDIR/annotations.$TYPE.all.agreement.gt.ct | grep full-agreement > $OUTDIR/annotations.$TYPE.all.agreement.gt.ct.fa
    jq -r '.pairid' < $OUTDIR/annotations.$TYPE.all.agreement.gt | tr "-" "\n" | sort | uniq > $OUTDIR/annotations.$TYPE.all.agreement.gt.songids
done
