# frequency.py
# Frequency analysis on a file
# 05/18/2017

import string

def histo(list_to_histo):
    val_lst = list()
    for key, val in list_to_histo:
        val_lst.append( (val, key) )
    scaling_factor = (max(val_lst)[0])/60
    for key, val in list_to_histo:
        print '{:2} {:5} {:6.2f}%'.format(key, val, (float(val) / total) * 100), 'x' * (val / scaling_factor)

fname = raw_input('Enter a file name: ')
if len(fname) < 1 : 
    fname = "cremation.txt"
    print 'Using default file', fname
try:
    fhand = open(fname)
except: 
    print 'File cannot be opened:', fname
    exit()

counts = dict()
total = 0
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.rstrip('\n')
    line = line.lower()
    for char in line:
        counts[char] = counts.get(char, 0) + 1
        total = total + 1

sorted_lst = sorted(counts.items())

print 'Total # of chars: ', total
print 'Number of unique chars: ', len(counts.keys())

histo(sorted_lst)