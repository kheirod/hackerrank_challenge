
def sum1(input):
    sum = 0
    for row in range (len(input)-1):
        for col in range(len(input[0])-1):
            sum = sum + input[row][col]

    return sum






arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
    
print sum1(arr)


