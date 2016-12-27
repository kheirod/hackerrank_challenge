import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


arr.reverse()
print ' '.join(['%s' % (arr[i]) for i in xrange(len(arr))])