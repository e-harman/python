#05/04/2017
plaintext = 'ibm'
#plaintext = 'abc'
shift = -1
ciphertext = ''

for char in plaintext:
    #print chr(ord(char) + shift)
    ciphertext+=(chr(ord(char) + shift))

print ciphertext