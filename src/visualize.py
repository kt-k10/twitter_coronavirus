#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
parser.add_argument('--output_path', default='output.png')  # Added to specify output path for PNG
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# prepare the data
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=False)

# only take the top 10 keys
top_items = items[:10]

# print the count values
for k, v in top_items:
    print(k, ":", v)

# generate the bar graph
keys = [item[0] for item in top_items]
values = [item[1] for item in top_items]

plt.barh(keys, values)
plt.xlabel('Count')
plt.ylabel('Key')
plt.title(f'Top 10 {args.key} Counts')

# save the plot as a PNG file
plt.savefig(args.output_path)

# Optionally, show the plot (remove if not needed)
plt.show()

