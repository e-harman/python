# Count the # of times a single word appears in a file
# 04/18/2017

def count_word(file_handle, word):
    count = 0
    for line in file_handle:
        pos = 0
        line = line.strip()
        line = line.lower()
        while pos <= len(line):
            pos = line.find(word, pos)
            if pos == -1:
                break
            pos = pos + 1
            count = count + 1
    return count

fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

search_word = raw_input('Enter a word to search for: ')

word_count = count_word(fhand, search_word)

print word_count
