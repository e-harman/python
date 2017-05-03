# Frequency analysis on a string
# 05/02/2017

import string

#text = "Four score"
text = "Four score and seven years ago, our fathers established upon this continent a Government subscribed in liberty and dedicated to the fundamental principle that all mankind are created equal"

counts = dict()
text = text.translate(None, string.punctuation)
text = text.lower()

for char in text:
    counts[char] = counts.get(char,0) + 1

sorted_keys = counts.keys()
sorted_keys.sort()

for key in sorted_keys:
    print key, counts[key]

print 'Number of unique chars: ', len(counts.keys())