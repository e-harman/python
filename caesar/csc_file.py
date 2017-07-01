# csc_file.py
# Encrypts and decrypts files using a Caesar Shift Cipher
# 05/07/2017

def get_file():
    fname = raw_input('  Enter a file name: ')
    return fname

def crypt(f_plain, f_cipher, shift_val):
    for line in f_plain:
        ciphertext = ''
        line = line.rstrip()
        for char in line:
            if ord(char) < 154:
                ciphertext+=(chr(ord(char) + shift_val))
        print ciphertext #Debug
        ciphertext = ciphertext + '\n'
        f_cipher.write(ciphertext)

# *******************************************************

# Get plaintext filename
print 'Choose the plaintext file to encrypt'
plaintext_fname = get_file()
try:
    fhand_plain = open(plaintext_fname)
except:
    print 'File cannot be opened:', plaintext_fname
    exit()

# Get ciphertext filename
print 'Choose the ciphertext file to create'
ciphertext_fname = get_file()
fhand_cipher = open(ciphertext_fname, 'w')

shift = int(raw_input('Enter a shift value between -30 and 30: '))

crypt(fhand_plain, fhand_cipher, shift)

# Cleaning up
fhand_plain.close()
fhand_cipher.close()
