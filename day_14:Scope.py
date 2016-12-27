class Difference:
    def __init__(self, a):
        self.__elements = a
        
        self.maximumDifference = 0 
    def computeDifference(self) :
        mdiff = 0 
        for i in xrange(len(a)) :
            for j in xrange(len(a)) :
                  if i!=j :
                        diff =abs(a[j]-a[i]) 
                        if diff > self.maximumDifference:
                              self.maximumDifference = diff 
        return self.maximumDifference     

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference

            
