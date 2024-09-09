print('Learn which app to use to connect to the external server.')

os = input('Type "1" for mac, "2" for, windows, or "3" for linux: ')

if os == '1':
    print('You will need to open up Terminal.')
    
elif os == '2':
    print('You will need to open up Command Prompt.')

elif os == '3':
    print('Linux? You know what to do!')

else:
    print(os, 'is unknown operating system. Try again!')
