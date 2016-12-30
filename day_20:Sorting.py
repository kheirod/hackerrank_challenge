import sys

count=0
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

for i in xrange(n):
    for j in range(n-1) :
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            count+=1

        
print "Array is sorted in "+ str(count) +" swaps."
print "First Element: " + str(min(a)) 
print "Last Element: " + str(max(a)) 
