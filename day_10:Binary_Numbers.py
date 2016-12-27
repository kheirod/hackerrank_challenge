import sys


n = int(raw_input().strip())
print max([len(x) for x in '{0:b}'.format(n).split('0')])
