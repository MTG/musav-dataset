import json
import sys
from krippendorff import alpha

nan = float("nan")

annotations = {}
annotators = set()
# We need a mapping to numerical values to make krippendorff code work.
mapping = { 'a': -1, 'ab': 0, 'b': 1 }

# Reads from standard input.
for line in sys.stdin:
    annotation = json.loads(line)

    tripletid = annotation['tripletid']
    songid_a = annotation['songid_a']
    songid_b = annotation['songid_b']
    annotator = annotation['annotator']
    result = annotation['higher_value']

    pairid = '-'.join([tripletid, songid_a, songid_b])
    annotations.setdefault(pairid, {})
    annotations[pairid][annotator] = result

    annotators.add(annotator)

# Goal: [[..annotator..], [..annotator..]]

values = []
for annotator in annotators:
    annotator_values = []
    for pairid in annotations:
        if annotator in annotations[pairid]:
            value = mapping[annotations[pairid][annotator]]
        else:
            value = nan
        annotator_values.append(value)
    values.append(annotator_values)

print('alpha (nominal):', round(alpha(values, level_of_measurement='nominal'), 6))
print('alpha (ordinal):', round(alpha(values, level_of_measurement='ordinal'), 6))
