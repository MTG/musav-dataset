import argparse
import sys
import json

parser = argparse.ArgumentParser(description='Evaluate model predictions')
parser.add_argument('predictions',
                    help='model predictions (tracks) jsonl file name')
parser.add_argument('groundtruth',
                    help='ground truth (pairwise track comparisons) jsonl file name')
args = parser.parse_args()

if args.groundtruth.count('arousal'):
    annotation_type = 'arousal'
elif args.groundtruth.count('valence'):
    annotation_type = 'valence'
else:
    print("Wrong filename (filename should include 'arousal' or 'valence' substring)")
    sys.exit()

predictions = {}
models = set()
for line in open(args.predictions):
    track_prediction = json.loads(line)
    songid = track_prediction['songid']
    model = track_prediction['model']
    models.add(model)

    if annotation_type == 'arousal':
        value = track_prediction['arousal_mean']
    elif annotation_type == 'valence':
        value = track_prediction['valence_mean']

    predictions.setdefault(songid, {})
    predictions[songid][model] = value

models = list(models)
print(f"Found predictions for models {models}")

results = {}
for model in models:
    results[model] = {'correct': 0, 'incorrect': 0}

skipped_ab = 0
skipped_ab_predictions = 0

total_pairs = 0

for line in open(args.groundtruth):
    gt = json.loads(line)
    total_pairs += 1
    a, b = gt['pairid'].split('-')

    # Skipping a=b annotations for simplicity.
    if gt['higher_value'] == 'ab':
        skipped_ab += 1
        continue

    for model in models:
        a_value = predictions[a][model]
        b_value = predictions[b][model]

        if a_value == b_value:
            skipped_ab_predictions += 1
            continue

        if gt['higher_value'] == 'a':
            if a_value > b_value:
                results[model]['correct'] += 1
            elif a_value < b_value:
                results[model]['incorrect'] += 1

        elif gt['higher_value'] == 'b':
            if a_value > b_value:
                results[model]['incorrect'] += 1
            elif a_value < b_value:
                results[model]['correct'] += 1

print("Annotation type:", annotation_type)
print("Total ground truth pairs:", total_pairs)
print(f'skipped ab ground truth: {skipped_ab}')
print(f'skipped ab predictions: {skipped_ab_predictions}')
print('% of correct pairs:')
for model in results:
    total = results[model]['correct'] + results[model]['incorrect']
    correct_perc = 100. * results[model]['correct'] / total
    print(f'{args.groundtruth}\t{model}\t{correct_perc:.02f}')
print()
