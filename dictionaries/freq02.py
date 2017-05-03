# Frequency analysis on a file
# 05/02/2017

import string

fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except: 
    print 'File cannot be opened:', fname
    exit()

counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.rstrip('\n')
    line = line.lower()
    for char in line:
        counts[char] = counts.get(char, 0) + 1

sorted_keys = counts.keys()
sorted_keys.sort()

for key in sorted_keys:
    print key, counts[key]

print 'Number of unique chars: ', len(counts.keys())