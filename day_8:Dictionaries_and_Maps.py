n = input()
phonebook=dict([map(str,raw_input().split()) for x in range(n)])
keys=[]

while True:
    try:
        kayt=raw_input()
        keys.append(kayt)
    except:
        break
    
for t in range(n) :
    if keys[t] in phonebook :
        print('%s=%s' % (keys[t], phonebook[keys[t]]))
    else :
        print 'Not found'
