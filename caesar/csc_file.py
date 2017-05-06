# csc_file.py
# Encrypts and decrypts files using a Caesar Shift Cipher
# 05/06/2017

def get_file():
    fname = raw_input('  Enter a file name: ')
    return fname

# *******************************************************

# Get plaintext filename
print 'Choose the plaintext file to encrypt'
plaintext_fname = get_file()
#print plaintext_fname #Debug
#exit()
try:
    fhand_plain = open(plaintext_fname)
except:
    print 'File cannot be opened:', plaintext_fname
    exit()


# Get ciphertext filename
print 'Choose the ciphertext file to create'
ciphertext_fname = get_file()
try:
    fhand_cipher = open(ciphertext_fname)
    print '  Warning: file already exists'
    exit()
    print '  End of try clause executing'
except:
    print 'Beginning of except clause executing' #Debug
    fhand_cipher = open(ciphertext_fname, 'w')
    print 'End of Except clause executing' #Debug

fhand_cipher.close()
exit()