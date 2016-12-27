def factorial(x) : 
    result = 1 
    while (x>1) : 
        result=result*x 
        x=x-1 
    return result

n = int(input())

print factorial(n)
