#!/usr/bin/env python3

import argparse
import glob
parser = argparse.ArgumentParser()
parser.add_argument('--keys',nargs='+',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()
args.input_paths = glob.glob('outputs/geoTwitter*.lang')

# import
import os
import json
from collections import Counter,defaultdict
import re
import matplotlib.pyplot as plt
from datetime import datetime

total = defaultdict(lambda: Counter())
for path in args.input_paths:
    date = '20' + re.search(r'\d{2}-\d{2}-\d{2}', path).group()

    with open(path) as f:
        tmp = json.load(f)
        for k in args.keys:
            counts = 0
            if k in tmp:
                for i in tmp[k]:
                    counts += tmp[k][i]
    total[k][date] = counts

data = json.dumps(total)
data = json.loads(data)

# normalize the data by the total values
if args.percent:
    for k in data[args.key]:
        data[args.key][k] /= data['_all'][k]

# plot graph
for k in args.keys:
    items = sorted(list(data[k].items()))
    x_axis = [datetime.strptime(item[0], '%Y-%m-%d') for item in items]
    y_axis = [item[1] for item in items]
    plt.plot(x_axis, y_axis, label = k)

plt.legend()
plt.ylabel("Count")
plt.xlabel("Day of the Year in 2020")
plt.title(f"Frequency of {', '.join(args.keys)} in 2020")
plt.savefig(f"hashtags_{'_'.join(args.keys)}.png")
