
def is_leap(year):

    if year<=1900 :

         print "Enter the year above 1900"

    elif year == 2000 or year == 2400 or year==3000  or year==3400 or year==4000 or year==4400 or year==5000:

        leap = True

    elif  year%100==0 :

        leap = False

    elif year%4==0 :

        leap = True

    else :

        leap = False

    return leap


year = int(raw_input("Enter the year above 1900 : "))
is_leap(year)
print is_leap(year)

#print (is_leap(year))
