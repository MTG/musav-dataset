# Songids, genre annotations and genre stats for the annotated chunks 000-006
cat data/chunks/*.chunk.00[0-6].songids > data/audio.chunk_000-006.songids
cat data/genres.jsonl | grep -f data/audio.chunk_000-006.songids > data/genres.chunk_000-006.jsonl
python3 scripts/stats_genres.py data/genres.chunk_000-006.jsonl > stats/genres.chunk_000-006.stats.tsv
