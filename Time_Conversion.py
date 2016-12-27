import sys


time = raw_input().strip()
time2= bytearray(time)
#07:05:45PM input 
#19:05:45 output
if time[8] == 'P' :
    g = str(time[0]+time[1])
    d = int(g)+12
    f=str(d)
    if time[0] == '1' and time[1] == '2' :
        time2[8] =' '
        time2[9] =' '
      
    else :
        time2[0:1] =f[0]
        time2[1] =f[1]
        time2[8] =' '
        time2[9] =' '
    print time2

elif time[8] == 'A' :
    time2[8] =' '
    time2[9] =' '
    if time[0] == '1' and time[1] == '2' :
        time2[0] ='0'
        time2[1] ='0'

    print time2