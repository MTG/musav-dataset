import json
import argparse
import sys

parser = argparse.ArgumentParser(description='Analyze raw annotations')
parser.add_argument('triplets_filename',
                    help='path to triplets metadata file (`triplets.jsonl`)')
args = parser.parse_args()

# Load triplet type metadata
triplets_type = {}
for line in open(args.triplets_filename):
    triplet_meta = json.loads(line)
    triplets_type[triplet_meta['tripletid']] = triplet_meta['triplet_type']

pairs = {}
triplets = {}
pairs_tripletid = {}

# Reads from standard input.
for line in sys.stdin:
    annotation = json.loads(line)
    pairid = annotation['songid_a'] + '-' + annotation['songid_b']
    pairs.setdefault(pairid, [])
    pairs[pairid].append(annotation['higher_value'])
    pairs_tripletid[pairid] = annotation['tripletid']
    triplets.setdefault(annotation['tripletid'], set())
    triplets[annotation['tripletid']].add(pairid)

for pairid in pairs:
    pairs[pairid].sort()

# Full agreement: all three annotators agree.
full_agreement = [['a', 'a', 'a'], ['ab', 'ab', 'ab'], ['b', 'b', 'b']]
# Majority agreement: two annotators agree and the other one does not radically contradict.
majority_agreement = [['a', 'a', 'ab'], ['ab', 'b', 'b'], ['a', 'ab', 'ab'], ['ab', 'ab', 'b']]

for pairid, pair in pairs.items():
    if pair in full_agreement:
        agreement = "full-agreement"
    elif pair in majority_agreement:
        agreement = "majority-agreement"
    elif len(pair) == 3:
        agreement = "disagreement"
    else:
        agreement = "incomplete"

    if pair.count('a') >= 2:
        outcome = 'a'
    elif pair.count('b') >= 2:
        outcome = 'b'
    elif pair.count('ab') >= 2:
        outcome = 'ab'
    else:
        outcome = 'undefined'

    tripletid = pairs_tripletid[pairid]
    d = { 'tripletid': tripletid, 'triplet_type': triplets_type[tripletid],
          'pairid': pairid, 'agreement': agreement, 'higher_value': outcome }

    print(json.dumps(d))
