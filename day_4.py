class Person():
    
    def __init__(self,initialAge=13):
        
        self.initialAge=initialAge
        if self.initialAge < 0 :
             print "Age is not valid, setting age to 0" 

    def amIOld(self):
         # Do some computations in here and print out the correct statement to the console
        
        if  -5 <= self.initialAge < 13 : 
        
               print "You are young"
        elif 13 <= self.initialAge < 18 :
               print "You are teenager"
        else :
                print "You are old"
    def yearPasses(self):
        self.initialAge = self.initialAge + 1 

t = int(raw_input())

for i in range(0, t):
    age = int(raw_input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()        
    p.amIOld()
   # print("")