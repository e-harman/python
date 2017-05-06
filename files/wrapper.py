'''
    File name: wrapper.py
    Author: Eric Harman
    Description: To wrap files with long lines to reasonable length
    Python version: 2.7
'''

import textwrap

def wrap_file(original_file_handle, length):
    newfile = fname + '_new.txt'
    try:
        new_file_handle = open(newfile, 'w')
    except:
        print 'Error opening new file', newfile
        exit()
    for line in original_file_handle:
        line = line.strip()
        wrapped_lines = textwrap.fill(line, length)
        print wrapped_lines
        wrapped_lines = wrapped_lines + '\n'
        new_file_handle.write(wrapped_lines)

fname = raw_input('Enter file to process: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

line_length = int(raw_input('Enter line length: '))

wrap_file(fhand, line_length)

