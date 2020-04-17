#!/usr/bin/env python
import sys
import datetime
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pyplot import figure

current_page_count = int(sys.argv[1])
target_date = sys.argv[2]
target_page_count = int(sys.argv[3])



days = []
for line in open('shame.dat', 'r'):
  days.append(line.split())

if len(days) > 0 and days[-1][0] == str(datetime.date.today()):
  days.pop()
days.append([str(datetime.date.today()), current_page_count])

f = open('shame.dat', 'w')
for day in days:
  f.write('%s %s\n' % (day[0], day[1]))
f.close()

pages = [days[0][1]]
for i in range(1, len(days)):
  then = datetime.datetime.strptime(days[i-1][0], '%Y-%m-%d')
  now = datetime.datetime.strptime(days[i][0], '%Y-%m-%d')
  while then + datetime.timedelta(days=1) < now:
    then = then + datetime.timedelta(days=1)
    pages.append(pages[-1])
  pages.append(days[i][1])

day_start = datetime.datetime.strptime(days[0][0], '%Y-%m-%d')
deadline = datetime.datetime.strptime(target_date, '%Y-%m-%d')
today = datetime.datetime.strptime(days[-1][0], '%Y-%m-%d')

max_days = int((deadline - datetime.datetime.strptime(days[0][0], '%Y-%m-%d')).days)
days_remaining = int((deadline - today).days)

interp_x = [0, len(pages)-1]
interp_y = [0, pages[-1]]
remaining_x = [len(pages)-1, max_days]
remaining_y = [pages[-1], int(sys.argv[3])]

pages_remaining = target_page_count - current_page_count
required_rate = float(pages_remaining) / days_remaining
current_rate = float(current_page_count) / (len(pages) - 1)

est_days_to_completion = float(pages_remaining) / current_rate

projection_x_end = min(max_days, float(target_page_count) / current_rate)
projection_x = [len(pages)-1, projection_x_end]
projection_y = [pages[-1], target_page_count]


if len(pages) > int(max_days):
  projection_x = []
  projection_y = []

#plt.ylim(0.0, 100.0)
print pages
print interp_x
print interp_y
print projection_x
print projection_y
print remaining_x
print remaining_y
plt.figure(figsize = (8,4))
plt.plot(pages, 'bo-', projection_x, projection_y, 'bo--', remaining_x, remaining_y, 'go--')
#plt.plot(pages, 'bo', interp_x, interp_y, 'b-', remaining_x, remaining_y, 'go--')

hacky_rot_scale = 1.65
required_degrees = (float(180) / np.pi) * np.arctan(hacky_rot_scale * required_rate)
current_degrees = (float(180) / np.pi) * np.arctan(hacky_rot_scale * current_rate)

text_x_offset = (projection_x_end - (len(pages) - 1))/2

text_orth_displacement = 3

def text_y(slope, above_the_line = True):
    sign = 1 if above_the_line else -1
    base  = float(slope) * text_x_offset
    theta = np.pi/2 - np.arctan(slope)
    return base + float(text_orth_displacement) / np.sin(theta) * sign

def text_x(slope, above_the_line = True):
    sign = 1 if above_the_line else -1
    base  = text_x_offset
    theta = np.pi/2 - np.arctan(slope)
    return base - np.cos(theta) * text_orth_displacement * sign

text_y_curr  = text_y(current_rate, current_rate > required_rate)
text_x_curr  = text_x(current_rate, current_rate > required_rate)
text_y_required  = text_y(required_rate, current_rate <= required_rate)
text_x_required  = text_x(required_rate, current_rate <= required_rate)

#text_props = {'ha': 'left', 'va': 'bottom'}
text_props = {'ha': 'center', 'va': 'center'}
#text_props = {}

# Required pages per day annotation
plt.text(len(pages) - 1 + text_x_required,
         pages[-1] + text_y_required,
         '{0:1.1f} pages/day'.format(required_rate),
         text_props,
         rotation=required_degrees,
         color = 'g')

# Current pages per day annotation
plt.text(len(pages) - 1 + text_x_curr,
         pages[-1] + text_y_curr,
         '{0:1.1f} pages/day'.format(current_rate),
         text_props,
         rotation=current_degrees,
         color = 'b')



xtick_days = [day_start]
for i in xrange(4,13):
    xtick_days.append(datetime.datetime(2020, i, 1))
xtick_days.append(deadline)

xtick_coords = []
xtick_labels = []
for i in range(len(xtick_days)):
    if (i == 0):
        xtick_coords.append(0)
    else:
        xtick_coords.append((xtick_days[i] - xtick_days[0]).days)

    xtick_labels.append("{}/{}".format(xtick_days[i].month, xtick_days[i].day))

print xtick_coords


#locs, labels = plt.xticks()
plt.xticks(xtick_coords, xtick_labels, rotation=45, text="Dates")
plt.xlabel('Date')
plt.ylabel('Pages Written')
plt.legend(['Actual', 'Projected', 'Required'])
plt.savefig('shame.png', dpi=160, format='png', bbox_inches='tight')
