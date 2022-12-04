# MusAV scripts

Install dependencies:
```
pip3 install -r scripts/requirements.txt
```

Run all scripts from the root directory of the repository.


## Evaluation of AV regression models

### Evaluation of AV values from Spotify API

Download the `metadata-spotifyapi_chunks` folder from [Zenodo](TODO URL) (unpack into `data/`).

Gather all AV predictions from the Spotify API metadata in one file:
```
./scripts/spotifyapi_av_predictions.sh
```
The results will be stored in `data/metadata-spotifyapi_chunks/av-predictions.spotifyapi.jsonl`.

Evaluate AV predictions agains the ground truth
```
./scripts/evaluate_all.sh
```

### To evaluate other models

You can evaluate predictions done by multiple models altogether. Create a file with predictions by all models for all annotated tracks in the MusAV dataset (all audio tracks in `audio_chunks/`) in the JSONL format similar to `av-predictions.spotifyapi.jsonl`:
```
{"songid": "02dMF381tQaidG17In1Tt2", "model": "my_model_1", "arousal_mean": 0.417, "valence_mean": 0.382}
{"songid": "02KPo7DqVnSTSZnKvdT5NU", "model": "my_model_1", "arousal_mean": 0.348, "valence_mean": 0.505}
{"songid": "03m6QzQ3fobO9rPbyeOITY", "model": "my_model_1", "arousal_mean": 0.706, "valence_mean": 0.67}
...
{"songid": "02dMF381tQaidG17In1Tt2", "model": "my_model_2", "arousal_mean": 0.146, "valence_mean": 0.359}
{"songid": "02KPo7DqVnSTSZnKvdT5NU", "model": "my_model_2", "arousal_mean": 0.523, "valence_mean": 0.477}
{"songid": "03m6QzQ3fobO9rPbyeOITY", "model": "my_model_2", "arousal_mean": 0.874, "valence_mean": 0.571}
...
```

Change the `PREDICTIONS` filepath in the `./scripts/evaluate_all.sh` script accordingly, and run it.


## Helper scripts used for dataset creation and stats

To create files with Spotify track IDs, genre annotations and genre stats for the annotated chunks 000-006:
```
./scripts/chunks_songids_genres.sh
```

To recreate processed annotation ground truth (agreement and triplet consistency):
```
./scripts/annotations_groundtruth.sh
```

Basic agreement stats (number of annotated track pairs with different level of agreement and triplet consistency):
```
wc -l data/annotations/annotations.*.agreement*
```

To compute agreement stats (global vs genre triplets):
```
scripts/stats_agreement_global_vs_genre.sh
```

To compute inter-annotator agreement (Krippendorff's alpha):
```
./scripts/stats_agreement_krippendorff.sh
```
