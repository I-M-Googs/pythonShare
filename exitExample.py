import sys
while True:
    print('Type exit to exit.\n')
    response = input()
    if response == 'exit':
        print('You typed ' + response + '.')
        sys.exit()
