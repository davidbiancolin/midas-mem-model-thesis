#!/usr/bin/env python

import re
import time
import sys
import json
import numpy as np
import argparse

# -------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Plot Java allocation timeseries')
parser.add_argument('--files', default=['data/java-timeseries-midas/pmd.series'], nargs='+',
        help='Files that contain the data to plot')
parser.add_argument('--out', default='java.pdf',
        help='Output file')
parser.add_argument('--sizes', default=[], type=int, nargs='*',
        help='If set, only consider these allocation sizes')
parser.add_argument('--average', default=0, type=int,
        help='Average results over these many cycles')
parser.add_argument('--ignore-time', action='store_true', default=False,
	help='Arrange x axis by allocation series, not time')
parser.add_argument('--xmin', metavar='N', type=float, default=0,
        help='Data range (in ms)')
parser.add_argument('--xmax', metavar='N', type=float, default=600,
        help='Data range (in ms)')
parser.add_argument('--ymax', metavar='N', type=float, default=-1,
        help='Data range')
parser.add_argument('--mode', default='latency', choices=['latency', 'allocrate', 'allocdata', 'addrtrace', 'colorlatency'],
	help='Type of data to plot: latency|allcrate')
args = parser.parse_args()

# -------------------------------------------------------------------------

def ignore_time(arr):
	for i in range(len(arr)):
		arr[i]['time'] = i

print 'Open ' + args.files[0]
with open(args.files[0], 'r') as fin:
	overflow = int(fin.readline().split(' ')[1])
	head = int(fin.readline().split(' ')[1])
	base = int(fin.readline().split(' ')[2])
	print 'Overflow: %d, Head: %d, Base Cycle: %d' % (overflow, head, base)
	lines = fin.readlines()

data = []
sizes = {}
cur_time = 0

for l in lines:
	els = l.split(' ')
	if args.ignore_time:
		cur_time += 1
	else:
		cur_time += int(els[0])
	data.append({'time':cur_time, 'size':int(els[1]), 'dur':int(els[2]), 'addr':int(els[3], 16)})
	sizes[int(els[1])] = 1

print '%d data points: %d -> %d' % (len(data), 0, cur_time)

if len(args.sizes) != 0:
	data = [x for x in data if x['size'] in args.sizes]
	print 'Filtered down to %d data points based on size' % len(data)

if args.mode == 'latency' and args.average > 0:
	print 'Averaging data...'
	newdata = []
	cur_time = 0
	cur_sum = 0
	for el in data:
		while el['time'] > cur_time + args.average:
			newdata.append({'time':cur_time, 'dur':cur_sum})
			cur_time += args.average
			cur_sum = 0
		cur_sum += el['dur']
	newdata.append({'time':cur_time, 'dur':cur_sum})
	data = newdata

if args.mode == 'allocrate' or args.mode == 'allocdata':
	print 'Calculating allocation rate...'
	newdata = []
	cur_time = 0
	cur_sum = 0
	cur_count = 0
	for el in data:
		while el['time'] > cur_time + args.average:
			newdata.append({'time':cur_time, 'dur':cur_sum})
			cur_time += args.average
			cur_sum = 0
			cur_count = 0
		if args.mode == 'allocdata':
			cur_sum += el['size']
			cur_count += 1
		else:
			cur_sum += 1
			cur_count = 1
	newdata.append({'time':cur_time, 'dur':float(cur_sum)/float(cur_count)})
	data = newdata


print 'Importing matplotlib, plotting output...'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import gridspec

if args.mode == 'addrtrace':
	plt.figure(figsize=(10,4))

	if len(args.sizes) > 0:
		my_sizes = args.sizes
	else:
		my_sizes = [x for x in sizes.keys() if x < 10000]

	print 'Plotting sizes: ', ', '.join([str(x) for x in my_sizes])
	for s in my_sizes:
		my_data = [x for x in data if x['size'] == s]
		plt.plot([x['time'] for x in my_data], [x['addr'] for x in my_data], linestyle='None', marker='.')
	plt.ylim(0x38000000, 0x40000000)
	plt.ylabel("Virtual Memory Address")
	plt.gca().get_yaxis().set_major_formatter(ticker.FormatStrFormatter("0x%x"))
	plt.xlim(args.xmin*1000000.0, args.xmax*1000000.0)
	plt.gca().get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/1000000.0)))
	plt.xlabel("Simulated time in ms (assuming 1 GHz clock rate)")
elif args.mode == 'colorlatency':
	if len(args.sizes) > 0:
		my_sizes = args.sizes
	else:
		my_sizes = [x for x in sizes.keys() if x < 10000]

	print 'Plotting sizes: ', ', '.join([str(x) for x in my_sizes])
	for s in my_sizes:
		my_data = [x for x in data if x['size'] == s]
		if args.ignore_time:
			ignore_time(my_data)
		xdata = [x['time'] for x in my_data]
		plt.xlim(args.xmin*1000000.0, args.xmax*1000000.0)
		plt.ylim(0, args.ymax)
		plt.plot(xdata, [x['dur'] for x in my_data])
else:
	if args.ignore_time:
		ignore_time(data)

	xdata = [x['time'] for x in data]
	plt.xlim(args.xmin*1000000.0, args.xmax*1000000.0)

	plt.ylabel("Allocation latency (in Kcycles)")
	plt.gca().get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/1000000.0)))
	plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/1000.0)))
	plt.xlabel("Simulated time in ms (assuming 1 GHz clock rate)")

	if args.ymax > 0:
		plt.ylim(0, args.ymax)
	plt.plot(xdata, [x['dur'] for x in data])

plt.savefig(args.out, dpi=400, bbox_inches='tight', pad_inches=0)
plt.clf()
