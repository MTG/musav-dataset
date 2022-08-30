#!/usr/bin/env bash
DIR=data/annotations

for TYPE in arousal valence
do
    echo --- $TYPE annotations ---
    for TRIPLET_TYPE in global_triplet genre_triplet
    do 
        global_pairs_total=`cat $DIR/annotations.$TYPE.all.agreement | grep $TRIPLET_TYPE | wc -l`
        global_pairs_agreement=`cat $DIR/annotations.$TYPE.all.agreement.gt | grep $TRIPLET_TYPE | wc -l`
        echo $TRIPLET_TYPE:
        echo "- Pairs annotated (total): $global_pairs_total"
        echo "- Pairs with agreement: $global_pairs_agreement ($((100 * $global_pairs_agreement/$global_pairs_total))%)"
    done
    echo
done
