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
