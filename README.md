# The MusAV Dataset

TODO Zenodo DOI badge

MusAV is a new public benchmark dataset for comparative validation of arousal and valence (AV) regression models for audio-based music emotion recognition.
We built MusAV by gathering comparative annotations of arousal and valence on pairs of tracks, using track audio previews and metadata from the Spotify API.
The resulting dataset contains 2,092 track previews covering 1,404 genres, with pairwise relative AV judgments by 20 annotators and various subsets of the ground truth based on different levels of annotation agreement.

This repository contains metadata, scripts, and instructions on how to download and use the dataset.


## Structure

### Data in [`data`](data)

- `audio.songids` - Spotify IDs for all 17,574 track previews in the annotation pool (initial candidates)
- `genres.jsonl` - genre annotations
- `audio.ebur128` - EBU R128 integrated loudness (computed with [Essentia](https://essentia.upf.edu/reference/std_LoudnessEBUR128.html))
- `audio.ebur128_-20-5.songids` - Spotify IDs for 15,979 track previews in the final annotation pool that are within typical [-20, -5] LUFS loudness range (tracks selected for annotation)
- `genres.ebur128_-20-5.jsonl` - their genre annotations
- `triplets.jsonl` - 5,326 triplets generated for these tracks. No track appears in more than one triplet. The triplets include:
	- *genre-triplets* (all tracks sharing the same genre, one triplet per genre)
	- *global-triplets* (the remaining tracks)

- `chunks/` - triplets split into annotation chunks
	- `triplets.global.chunk.*` - global-triplets
	- `triplets.genre.chunk.*` - genre-triplets
	- `triplets.all.chunk.*.songids` - Spotify IDs
	- `triplets.all.chunk.*.pairs` - annotation pairs for triplets (each record contains a pair ID and song A/B ID, audio filepath, and loudness)

- `genres.chunk_000-006.jsonl` - genre annotations for tracks in chunks 000-006

- `annotations/` - human AV annotations for chunks 000-006
	- `annotations.@(arousal|valence).all`  - raw comparative annotations on track pairs by anonymized annotators (6,255 pairs). 
	- `annotations.@(arousal|valence).all.agreement` - processed annotations on track pairs with different level of agreement: disagreement, majority-agreement (MA), full-agreement (FA)
	- `annotations.@(arousal|valence).all.agreement.gt`  - all annotations considered ground truth (pairs with either FA or MA with/without triplet consistency)
	- `annotations.@(arousal|valence).all.agreement.gt.ct` - ground-truth annotations with FA/MA and triplet consistency
	- `annotations.@(arousal|valence).all.agreement.gt.ct.fa` - ground-truth annotations with FA and triplet consistency

- `audio_chunks/` (764 MB) and `annotations-spotifyapi_chunks/` (1.3 GB) - audio track previews and metadata gathered from the Spotify API for the annotated chunks 000-006 (2,100 tracks). Download these folders from Zenodo. Available under request for non-commercial scientific research purposes only. Any publication of results based on this data must cite Spotify API as the source of the data.


## Citing the dataset

Please consider citing [the following publication](TODO) when using the dataset:

> Bogdanov, D., Lizarraga-Seijas, X., Alonso-Jiménez, P., & Serra X. (2022). MusAV: A dataset of relative arousal-valence annotations for validation of audio models. International Society for Music Information Retrieval Conference (ISMIR 2022).

```
@conference {bogdanov2019mtg,
    author = "Bogdanov, Dmitry and Lizarraga-Seijas, Xavier and Alonso-Jiménez, Pablo and Serra, Xavier",
    title = "MusAV: A dataset of relative arousal-valence annotations for validation of audio models",
    booktitle = "International Society for Music Information Retrieval Conference (ISMIR 2022)",
    year = "2022",
    address = "Bengaluru, India",
    url = "TODO"
}
```


## License TODO

Copyright 2022 Music Technology Group


## Acknowledgments

TODO grants. We thank all the annotators who participated in the creation of the dataset.