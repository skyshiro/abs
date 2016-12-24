#! python3

PASSWORDS = {'email': '123',
             'blog' : 'abc',
             'luggage' : '456'}

import sys,pyperclip
if len(sys.argv)< 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
    
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
