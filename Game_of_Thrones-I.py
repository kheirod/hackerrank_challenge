import sys
from collections import Counter
string = raw_input()
 
found = False
n = len(string)
count = 0
c = Counter(string)
for key in c:
    if c[key]%2 == 0:
        count += 1
if count == len(c) and n%2 == 0:
    found = True
elif count == len(c)-1 and n%2 == 1:
    found = True

if not found:
    print("NO")
else:
    print("YES")
