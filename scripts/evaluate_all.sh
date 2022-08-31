PREDICTIONS=data/metadata-spotifyapi_chunks/av-predictions.spotifyapi.jsonl
ANNOTATIONS_DIR=data/annotations

python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.arousal.all.agreement.gt
python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.arousal.all.agreement.gt.fa
python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.arousal.all.agreement.gt.ct
python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.arousal.all.agreement.gt.ct.fa

python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.valence.all.agreement.gt
python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.valence.all.agreement.gt.fa
python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.valence.all.agreement.gt.ct
python3 scripts/evaluate.py $PREDICTIONS $ANNOTATIONS_DIR/annotations.valence.all.agreement.gt.ct.fa
