#!/usr/bin/env bash

for f in `find data/metadata-spotifyapi_chunks/ -name "*.yaml" | sort`; do energy=`yq .audio_features.energy $f`; valence=`yq  .audio_features.valence $f`; songid=${f//*metadata-spotifyapi_chunks\/*\//}; songid=${songid//.yaml/}; echo "{\"songid\": \"$songid\", \"model\": \"spotifyapi\", \"arousal_mean\": $energy, \"valence_mean\": $valence}"; done > data/metadata-spotifyapi_chunks/av-predictions.spotifyapi.jsonl
