if __name__ == '__main__':
    n = int(raw_input())

    if n == 3 or n == 5 or n==29:
        print "Weird"
    elif 2 <= n < 5 :
        print "Not Weird"
    elif 6 <= n <= 20 :
        print "Weird"
    elif 20 < n :
        print "Not Weird"
    else :
        print "Not Weird"
