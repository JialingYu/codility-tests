#method 1: O(N*log(N)) or O(N)
from collections import defaultdict
def solution(A):
    #initialize a default dict with value 0
    count=defaultdict(int)
    l=len(A)
    for key, value in enumerate(A):
        count[value]+=1
        #if the count of the value is bigger than half of the length of A
        if count[value] > l//2:
            #return the index
            return key
    return -1

#method 2:O(N) or O(NlogN)
def solution(A):
    n=len(A)
    if n==0:
        return -1
    if n==1:
        return 0
    #use the fact that removing a pair of distinct elements from A would not change the leader of A
    #create an empty stack to stack elements of A such that distinct elements are removed and only the same values left
    #this value would be the candidate for leader
    #in order to check whether it is a leader, we need to iterate A and count the number of the value
    #if it is > n/2, it is a leader, else there is no leader
    s=[]
    for i in range(n):
        #if s is empty or the current A[i] equal to the last element of the s, append A[i] to s
        if len(s)==0 or A[i]==s[-1]:
            s.append(A[i])
        #otherwise A[i] is not equal to the last element of s and remove the last element from s
        else:
            s.pop()
    if len(s)==0:
        return -1
    else:
        candidate=s[0]
        c=0
        ind=-1
        for i in range(n):
            if A[i]==candidate:
                c+=1
                ind=i
        if c>n/2:
            return ind
        else:
            return -1
