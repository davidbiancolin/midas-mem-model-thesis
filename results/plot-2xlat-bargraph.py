#!/usr/bin/env python

import re
import time
import sys
import json
import argparse

# -------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Plot Java memory timeseries')
parser.add_argument('--latency', default='data/rocket.java.2x-lat/',
        help='Directory that contains the baseline data')
parser.add_argument('--baseline', default='data/rocket.java.trace/',
        help='Directory that contains the baseline data')
parser.add_argument('--benchmarks', nargs='+', default=['avrora', 'pmd', 'sunflow', 'luindex', 'lusearch', 'xalan'],
        help='Directory that contains the baseline data')
parser.add_argument('--out', default='dacapo-varymodel.pdf',
        help='Output file')
args = parser.parse_args()

# -------------------------------------------------------------------------

benchmarks = args.benchmarks

def read_file(filename):
	print 'Open ' + filename

	gc_time = 0.0
	total_time = 0.0
	with open(filename, 'r') as fin:
		lines = fin.readlines()
		for l in lines:
			if l.startswith('[GC '):
				els = l.split(" ")
				gc_time += float(els[12])
			else:
				m = re.search('PASSED in (.+) msec', l)
				if m != None:
					total_time = float(m.group(1))

	print filename, ' -> ', (total_time, gc_time)
	return (total_time, gc_time)

total_times = {'baseline':[], '2xlat':[]}
gc_times = {'baseline':[], '2xlat':[]}

for (run, f) in [('baseline', args.baseline), ('2xlat', args.latency)]:
	for bm in benchmarks:
		filename = '%s/%s.out' % (f, bm)
		(x,y) = read_file(filename)
		total_times[run].append(x)
		gc_times[run].append(y)

import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

print 'Plotting graph...'

# These are the "Tableau 20" colors as RGB.  
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),  
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),  
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),  
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),  
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]  
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.  
for i in range(len(tableau20)):  
    r, g, b = tableau20[i]  
    tableau20[i] = (r / 255., g / 255., b / 255.)  

plt.figure(figsize=(10,3))

bar_width = 0.3

ind = numpy.arange(len(benchmarks))

plt.ylabel('Slowdown')
#plt.title('Runtime and Number of Full GCs per Superstep')
#plt.xticks(index + bar_width, index)
plt.xticks(ind+bar_width, benchmarks)
plt.xlim(-0.3, len(ind))
plt.ylim(1.0, 1.2)

plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{0:g}%'.format((x-1)*100.0)))

rects1 = plt.bar(ind+0.1, [total_times['2xlat'][i] / total_times['baseline'][i] for i in range(len(benchmarks))], bar_width,
		 color=tableau20[2],
                 label='Overall Benchmark')

rects1 = plt.bar(ind+0.5, [gc_times['2xlat'][i] / gc_times['baseline'][i] for i in range(len(benchmarks))], bar_width,
		 color=tableau20[0],
                 label='GC Portion')

plt.legend(loc='upper center', ncol=2)

#rects1 = plt.bar(ind+bar_width+0.02, [data['master'][i] / data['baseline'][i] for i in range(len(benchmarks))], bar_width, \
#		 yerr=[yerr['master'][i] / data['baseline'][i] for i in range(len(benchmarks))], ecolor='black', \
#		 color=tableau20[0],
#                label='Leader')

plt.tight_layout()

plt.savefig(args.out, format='pdf', bbox_inches='tight', pad_inches=0)
plt.clf()
