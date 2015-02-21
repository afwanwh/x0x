from py_lib_chiper import *


print 'Welcome to Shift Chiper 1.0'
print 'What do you want?\n1. Encrypt a text\n2. Decrypt a code'
choice = raw_input('Enter your choice: ')
if choice == '1':
    txt = raw_input('Enter your text to encrypt: ')
    key = raw_input('Enter your key (must a number): ')
    try:
        if int(key):
            print 'Your chiper text: ' + encrypt_shift(key, txt)
    except ValueError:
        print "Key must an integer number!"
elif choice == '2':
    txt = raw_input('Enter your text to decrypt: ')
    key = raw_input('Enter your key (must a number): ')
    try:
        if int(key):
            print 'Your plain text: ' + decrypt_shift(key, txt)
    except ValueError:
        print "Key must an integer number!"
else:
    print 'Wrong choice, please choice 1 or 2'
