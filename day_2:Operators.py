mealcost = float(input())
tippercent = float(input())
tawpercent = float(input())

tip=(mealcost*tippercent)/100
tax=(mealcost*tawpercent)/100
total=(mealcost+tip+tax)
total2=round(total,0)

print "The total meal cost is",int(total2),"dollars."
