from lib import py_shift_chiper as psc


print 'Welcome to Shift Chiper 1.0'
print 'What do you want?\n1. Encrypt a text\n2. Decrypt a code'
choice = raw_input('Enter your choice: ')
if choice == '1':
    txt = raw_input('Enter your text to encrypt: ')
    key = raw_input('Enter your key (must a number): ')
elif choice == '2':
    txt = raw_input('Enter your text to decrypt: ')
    key = raw_input('Enter your key (must a number): ')
else:
    print 'Wrong choice, please choice 1 or 2'
