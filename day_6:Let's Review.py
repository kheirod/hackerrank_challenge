

t = int(raw_input())

for i in range(0, t):
    S=raw_input()
    x='' 
    y=''
    for i in range(len(S)):
        if i%2==0 :
            x=x+S[i]
        else :
            y=y+S[i]

    print x + ' ' +y


    
