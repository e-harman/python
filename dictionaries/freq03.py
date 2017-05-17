# freq03.py
# Frequency analysis on a file
# 05/16/2017
# Copy of freq02.py, adding histogram

import string

def histo(list_to_histo):
    val_lst = list()
    for key, val in list_to_histo:
        val_lst.append( (val, key) )
    #print max(val_lst)[0] #Debug
    scaling_factor = (max(val_lst)[0])/60
    #print scaling_factor #Debug
    for key, val in list_to_histo:
        print key, 'x' * (val / scaling_factor)

fname = raw_input('Enter a file name: ')
if len(fname) < 1 : fname = "cremation.txt"
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

#Now let's try newer techniques from chapter 10
sorted_lst = sorted(counts.items())

for key, val in sorted_lst:
    #print key, val
    #print key, val, round((float(val) / total) * 100,2)
    #print '%s %4d %#4.2g' % (key, val, round((float(val) / total) * 100,2))
    print '%s %4d % 3.2f' % (key, val, (float(val) / total) * 100)
print 'Total # of chars: ', total
print 'Number of unique chars: ', len(counts.keys())

histo(sorted_lst)