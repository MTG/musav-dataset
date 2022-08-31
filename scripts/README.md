# MusAV scripts

Install dependencies:
```
pip3 install -r scripts/requirements.txt
```

Run all scripts from the root directory of the repository.


## Evaluation of AV values from Spotify API

Download the `metadata-spotifyapi_chunks` folder from Zenodo.

Gather all AV predictions from the Spotify-API metadata in one file:
```
./scripts/spotifyapi_av_predictions.sh
```
The results will be stored in `metadata-spotifyapi_chunks/av-predictions.spotifyapi.jsonl`.


## Helper scripts for dataset creation and stats

To create files with songids, genre annotations and genre stats for the annotated chunks 000-006:
```
./scripts/chunks_songids_genres.sh
```

To recreate processed annotation ground truth (agreement and triplet consistency):
```
./scripts/annotations_groundtruth.sh
```

To compute agreement stats (global vs genre triplets):
```
scripts/stats_agreement_global_vs_genre.sh
```
