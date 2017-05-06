# Slices
# 04/15/2017
# Puzzle: What is the nth word?
# Between the n-1th and nth space

#Probably could have been done better with .split
#That also deals with multi-space separators automatically

#string = 'There are strange things done in the midnight sun By the men who moil for gold'
#string = 'hello'
#string = 'hello there'
string = 'hello    there     kids,   wow'
word_number = 4

#String preprocessing
string = string.strip()
string = " ".join(string.split())
#print 'Preprocessed string:', string #Debug
#Still need to remove punctuation

#Count number of words
word_count = 1
for letter in string:
    if letter == ' ':
        word_count = word_count + 1

#Add check for word_count < word_number, error so quit
if word_count < word_number:
    print 'Error: String contains fewer words than word number requested'
    print 'Number of words in string:', word_count
    print 'Word number requested:', word_number
    exit()

#Some ifs here (4 choices: 1-word string, 1st word, last word, any other
if word_count == 1:
    word = string
elif word_number == 1: #first word
    first_space = 0
    first_space = string.find(' ')
    word = string[:first_space]
elif word_number == word_count: #last word
    last_space = len(string) - 1
    while True:
        if string[last_space] == ' ':
            break
        last_space = last_space - 1
        word = string[last_space + 1:]
else: #this is the main case
    i = 0
    start_pos = 0
    while i < word_number-1:
        start_pos = string.find(' ',start_pos + 1)
        i = i + 1
    #print start_pos #Debug
    end_pos = string.find(' ',start_pos+1)
    #print end_pos #Debug
    word = string[start_pos+1:end_pos+1]

print 'Number of words in string: ', word_count
print 'Word number requested:     ', word_number
print 'Word is:', word