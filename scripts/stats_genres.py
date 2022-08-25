import argparse
import json
from collections import Counter


def stats_genres(genres_file):
    counter = Counter()
    with open(genres_file) as f:
        for track_json in f:
            counter.update(json.loads(track_json)['genres'])
    for genre, count in counter.most_common():
        print(f'{genre}\t{count}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Computes genre statistics (number of tracks per genre)')
    parser.add_argument('genres_file', help='genres metadata JSONL')
    args = parser.parse_args()
    stats_genres(args.genres_file)
