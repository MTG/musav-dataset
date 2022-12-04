# The MusAV Dataset

**NOTE** The dataset will be published online on December 4. Thanks for visiting!

TODO Zenodo DOI badge

MusAV is a new public benchmark dataset for comparative validation of arousal and valence (AV) regression models for audio-based music emotion recognition.
We built MusAV by gathering comparative annotations of arousal and valence on pairs of music tracks, using track audio previews and metadata from the Spotify API.
The resulting dataset contains 2,092 track previews covering 1,404 genres, with pairwise relative AV judgments by 20 annotators and various subsets of the ground truth based on different levels of annotation agreement.

This repository contains metadata, scripts, and instructions on how to download and use the dataset.


## Structure

Read the [ISMIR 2022 publication](#citing-the-dataset) for more details about the dataset creation and annotation process. You can also check our [ISMIR 2022 presentation materials](https://ismir2022program.ismir.net/poster_286.html) (poster, video).

### Data in [`data`](https://github.com/MTG/musav-dataset/tree/dev/data)

We provide metadata for the entire annotation pool (a preselection of music tracks for annotation) we used to create the dataset, organized into triplets of tracks and split into chunks.

We have gathered human arousal/valence pairwise relative annotations for **chunks 001-006**, with three participating human annotators for each chunk. The dataset includes audio previews and Spotify API metadata for the annotated chunks. Please, contact us if you want to expand the dataset by annotating more chunks.

The data is organized in TSV and JSONL formats as follows:

- `audio.songids` - Spotify IDs for all 17,574 track previews in the annotation pool (initial list of candidate tracks for annotation)
- `genres.jsonl` - corresponding genre annotations
- `audio.ebur128` - EBU R128 integrated loudness (computed with [Essentia](https://essentia.upf.edu/reference/std_LoudnessEBUR128.html))
- `audio.ebur128_-20-5.songids` - Spotify IDs for 15,979 track previews in the final annotation pool (tracks within a typical loudness range of [-20, -5] LUFS, selected for annotation)
- `genres.ebur128_-20-5.jsonl` - corresponding genre annotations
- `triplets.jsonl` - 5,326 triplets generated for these tracks. No track appears in more than one triplet. The triplets include *genre-triplets* (all tracks sharing the same genre, one triplet per genre) and *global-triplets* (the remaining tracks)

- `chunks/` - triplets split into annotation chunks
	- `triplets.global.chunk.*` - global-triplets
	- `triplets.genre.chunk.*` - genre-triplets
	- `triplets.all.chunk.*.songids` - Spotify IDs
	- `triplets.all.chunk.*.pairs` - annotation pairs for triplets (each record contains a pair ID and song A/B ID, audio filepath, and loudness)

- `genres.chunk_000-006.jsonl` - genre annotations for tracks in chunks 000-006
- `audio.chunk_000-006.songids` - Spotify IDs for tracks in chunks 000-006

- `annotations/` - human AV annotations for chunks 000-006
	- `annotations.@(arousal|valence).all`  - raw comparative annotations on track pairs by anonymized annotators (6,255 pairs). 
	- `annotations.@(arousal|valence).all.agreement` - processed annotations on track pairs with different level of agreement: disagreement, majority-agreement (MA), full-agreement (FA)
	- `annotations.@(arousal|valence).all.agreement.gt`  - all annotations considered ground truth (pairs with either FA or MA with/without triplet consistency)
	- `annotations.@(arousal|valence).all.agreement.gt.ct` - ground-truth annotations with FA/MA and triplet consistency
	- `annotations.@(arousal|valence).all.agreement.gt.ct.fa` - ground-truth annotations with FA and triplet consistency

    - `ismir2022/` - ground truth used to report evaluation results in the ISMIR 2022 publication (discarded tracks that belong to the MuSe dataset, which was used to train some of the evaluated models).

- ([Zenodo](TODO URL)) `audio_chunks/` (764 MB) and `metadata-spotifyapi_chunks/` (1.3 GB) - audio track previews and metadata gathered from the Spotify API for the annotated chunks 000-006 (2,100 tracks). Download these archived folders from Zenodo and unpack them into `data/` (available under request).


### Scripts in [`scripts`](scripts)


### Statistics in [`stats`](https://github.com/MTG/musav-dataset/tree/dev/stats)

- `genres.chunk_000-006.stats.tsv` - genre occurrences (number of tracks) in the annotated chunks 000-006


## Citing the dataset

Please consider citing [the following ISMIR 2022 publication](http://hdl.handle.net/10230/54181) when using the dataset:

> Bogdanov, D., Lizarraga-Seijas, X., Alonso-Jiménez, P., & Serra X. (2022). MusAV: A dataset of relative arousal-valence annotations for validation of audio models. International Society for Music Information Retrieval Conference (ISMIR 2022).

```
@conference {bogdanov2019mtg,
    author = "Bogdanov, Dmitry and Lizarraga-Seijas, Xavier and Alonso-Jiménez, Pablo and Serra, Xavier",
    title = "MusAV: A dataset of relative arousal-valence annotations for validation of audio models",
    booktitle = "International Society for Music Information Retrieval Conference (ISMIR 2022)",
    year = "2022",
    address = "Bengaluru, India",
    url = "http://hdl.handle.net/10230/54181"
}
```


## License

- The AV annotations metadata is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
- The audio track previews and Spotify API metadata are released for non-commercial scientific research purposes only. Any publication of results based on the data extracts of the Spotify database must cite Spotify as the source of the data.


## Acknowledgments

This research was carried out under the project Musical AI - PID2019-111403GB-I00/AEI/10.13039/501100011033, funded by the Spanish Ministerio de Ciencia e Innovación and the Agencia Estatal de Investigación.

We thank all the annotators who participated in the creation of the dataset.
