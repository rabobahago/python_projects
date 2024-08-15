import sys
try:
    n = int(sys.argv[1])
except:
    sys.exit('Please enter an integer , <n>, on the command line.\nUsage: ''python {:s} <n>'.format(sys.argv[0]))

print(n, 'squared is', n**2)