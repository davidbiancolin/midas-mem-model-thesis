#!/usr/bin/env python

import re
import time
import sys
import json
import numpy as np
import argparse
import csv

# -------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Plot Java memory timeseries')
parser.add_argument('--files', default=['data/output-MAS-open/pmd_memory_stats.csv'], nargs='+',
        help='Files that contain the data to plot')
parser.add_argument('--gcpauses', default=['data/output-MAS-open/pmd.out'], nargs='+',
        help='Files that contains the GC pauses to plot')
parser.add_argument('--out', default='memory.png',
        help='Output file')
parser.add_argument('--xmin', metavar='N', type=float, default=0,
        help='Data range (in ms)')
parser.add_argument('--xmax', metavar='N', type=float, default=600,
        help='Data range (in ms)')
parser.add_argument('--ymax', metavar='N', type=float, default=-1,
        help='Data range')
parser.add_argument('--delta', action='store_true', default=False,
	help='Plot deltas between time steps rather than absolute values')
args = parser.parse_args()

# -------------------------------------------------------------------------

print 'Open ' + args.files[0]

field = '// rowMisses'

gc_start_times = [
(5.01, 1309.03),
(10.08, 1486.44),
(16.90, 1648.14),
(26.08, 1944.43),
(34.02, 2196.24),
(43.63, 2454.38),
(56.03, 2660.56),
(72.84, 3162.73),
(91.00, 3410.81),
(112.85, 4003.80)
]

gc_offset = 400

if len(args.gcpauses) > 0:
	gc_start_times = []
	with open(args.gcpauses[0], 'r') as fin:
		lines = fin.readlines()
		for l in lines:
			if not l.startswith('[GC '):
				continue
			els = l.split(" ")
			gc_start_times.append((float(els[3]), float(els[12])))

	print 'GC Start times: ', gc_start_times

def get_value(row):
	return float(row['// rowMisses']) / float(int(row[' totalWrites']) + int(row[' totalReads']))

def delta(a, b):
	result = {}
	for k in a.keys():
		result[k] = int(a[k]) - int(b[k])
	return result

data = []
prev = None
with open(args.files[0], 'r') as fin:
	csvdata = csv.DictReader(fin)
	printed_keys = False

	for row in csvdata:
		if not printed_keys:
			print 'Found keys: '
			for k in row.keys():
				print k
			print 'Selected field: ', field
			printed_keys = True

		if args.delta and prev != None:
			data.append(get_value(delta(row, prev)))
		else:
			data.append(int(row[field]))

		prev = row

print 'Importing matplotlib, plotting output...'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import gridspec

plt.plot(range(len(data)), data, color='black')
plt.xlim(600, max([x+(y/1000.0) for (x, y) in gc_start_times])*100.0 + 600.0)
plt.ylim(0, 1)

plt.gca().get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/100.0)))
plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{0:g}%'.format(x*100.0)))
plt.xlabel("Simulated time in seconds (assuming 1 GHz clock rate)")
plt.ylabel("DRAM Row Miss Rate")

for (x,y) in gc_start_times:
	plt.axvspan(gc_offset + x*100, gc_offset + (x*100+y/10), color='green', alpha=0.5)

plt.savefig(args.out, dpi=400, bbox_inches='tight', pad_inches=0)
plt.clf()
