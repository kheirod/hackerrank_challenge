class Calculator() :
    def power(self, N_val, P_val):
        if N_val < 0 or P_val < 0 :
            raise Exception("n and p should be non-negative")
        else :
            return N_val ** P_val
        


myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e    
    