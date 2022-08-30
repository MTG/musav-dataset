import json
import sys

pairs = {}
triplets = {}

# Reads from standard input.
for line in sys.stdin:
    annotation = json.loads(line)
    tripletid, pairid = annotation['tripletid'], annotation['pairid']

    triplets.setdefault(tripletid, set())
    triplets[tripletid].add(pairid)
    pairs[pairid] = annotation


for tripletid, triplet_pairs in triplets.items():
    triplet_pairs = list(triplet_pairs)

    # Skipping triplets without annotator agreement on all three pairs.
    if len(triplet_pairs) < 3:
        for pairid in triplet_pairs:
            pairs[pairid]['triplet_consistency'] = 'incomplete'
            print(json.dumps(pairs[pairid]))
        continue

    # Take the first pair and define tracks A and B so that A >= B.
    pairid = triplet_pairs[0]
    trackids = pairid.split('-')
    if pairs[pairid]['higher_value'] in ['a', 'ab']:
        a, b = trackids[0], trackids[1]
    elif pairs[pairid]['higher_value'] == 'b':
        a, b = trackids[1], trackids[0]
    # Define track C as the other track left in the triplet.
    trackids = triplet_pairs[1].split('-')
    if trackids[0] not in [a, b]:
        c = trackids[0]
    else:
        c = trackids[1]

    # Recode and reorder comparisions in a more handy way.
    mapping = {a: 'a', b: 'b', c: 'c'}
    comparisons = []

    recode = {
        'b<a': 'a>b',
        'b>a': 'a<b',
        'b=a': 'a=b',
        'a<c': 'c>a',
        'a>c': 'c<a',
        'a=c': 'c=a',
        'c<b': 'b>c',
        'c>b': 'b<c',
        'c=b': 'b=c'}

    for pairid in triplet_pairs:
        ta, tb = pairid.split('-')
        if pairs[pairid]['higher_value'] == 'a':
            s = f'{mapping[ta]}>{mapping[tb]}'
        elif pairs[pairid]['higher_value'] == 'b':
            s = f'{mapping[ta]}<{mapping[tb]}'
        elif pairs[pairid]['higher_value'] == 'ab':
            s = f'{mapping[ta]}={mapping[tb]}'
        if s in recode:
            s = recode[s]
        comparisons.append(s)

    # All possible comparison cases and their consistency.
    consistency_cases = {
        'a>b b>c c>a': 'inconsistent',
        'a>b b>c c<a': 'consistent',
        'a>b b>c c=a': 'inconsistent',

        'a>b b<c c>a': 'consistent',
        'a>b b<c c<a': 'consistent',
        'a>b b<c c=a': 'consistent',

        'a>b b=c c>a': 'inconsistent',
        'a>b b=c c<a': 'consistent',
        'a>b b=c c=a': 'inconsistent',

        'a=b b>c c>a': 'inconsistent',
        'a=b b>c c<a': 'consistent',
        'a=b b>c c=a': 'inconsistent',

        'a=b b<c c>a': 'consistent',
        'a=b b<c c<a': 'inconsistent',
        'a=b b<c c=a': 'inconsistent',

        'a=b b=c c>a': 'inconsistent',
        'a=b b=c c<a': 'inconsistent',
        'a=b b=c c=a': 'consistent'
    }

    comparisons.sort()
    consistency = consistency_cases[' '.join(comparisons)]

    for pairid in triplet_pairs:
        pairs[pairid]['triplet_consistency'] = consistency
        print(json.dumps(pairs[pairid]))
