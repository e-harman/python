# Count the # of times a single word appears in a file
# 04/18/2017
# 04/20/2017: has bug(s)
#   Doesn't count word if there is punctuation after, 'gold;' for instance

def count_word(file_handle, word):
    count = 0
    for line in file_handle:
        pos = 0
        line = line.strip()
        line = line.lower()
        while pos <= len(line) - 1:
            pos = line.find(word, pos)
            if pos == -1:
                break
            # In the line below replace ==' ' with 'in' a list?
            if ((pos - 1 == -1) or (line[pos - 1] == ' ')) and ((pos + len(word) == len(line)) or (line[pos + len(word)] == ' ')):
                count = count + 1
            pos = pos + 1
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
