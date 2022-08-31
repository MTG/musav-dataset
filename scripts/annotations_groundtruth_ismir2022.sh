#!/usr/bin/env bash

INDIR=data/annotations
OUTDIR=data/annotations/ismir2022

for TYPE in arousal valence
do
    cat $INDIR/annotations.$TYPE.all.agreement.gt | grep -v -f $OUTDIR/ismir2022-muse.songids > $OUTDIR/annotations.$TYPE.all.agreement.gt
    cat $INDIR/annotations.$TYPE.all.agreement.gt.ct | grep -v -f $OUTDIR/ismir2022-muse.songids > $OUTDIR/annotations.$TYPE.all.agreement.gt.ct
    cat $INDIR/annotations.$TYPE.all.agreement.gt.fa | grep -v -f $OUTDIR/ismir2022-muse.songids > $OUTDIR/annotations.$TYPE.all.agreement.gt.fa
    cat $INDIR/annotations.$TYPE.all.agreement.gt.ct.fa | grep -v -f $OUTDIR/ismir2022-muse.songids > $OUTDIR/annotations.$TYPE.all.agreement.gt.ct.fa
    cat $INDIR/annotations.$TYPE.all.agreement.gt.songids | grep -v -f $OUTDIR/ismir2022-muse.songids > $OUTDIR/annotations.$TYPE.all.agreement.gt.songids
done
