import sys 

class Solution:
    # Write your code here
    def __init__(self):
        self.push=[]
        self.enqueue=[]
        self.rev=[]
    
    def pushCharacter(self,pu):
        self.push.append(pu)
        
    def enqueueCharacter(self,enq) :
        self.enqueue.append(enq)
        
    def popCharacter(self):
        l = len(self.push)
        stack = self.push[l-1]
        del(self.push[l-1])
        return stack
    
   
    def dequeueCharacter(self):
        Queue=self.enqueue[0]
        del self.enqueue[0]
        return Queue

# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.\n")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.\n")  
    