#method1: O(sqrt(N))
def solution(N):
    #the factors of N appears in pairs; if a is a factor, N/a would also be a factor
    #the smaller factor of among the pair would be <=sqrt(N)
    import math
    c=0
    i=1
    while i < math.sqrt(N):
        if N%i==0:
            c+=2
        i+=1
    #if sqrt(N) is an integer, it would also be a factor
    if int(math.sqrt(N))==math.sqrt(N):
        c+=1
    return c

#method2:O(sqrt(N))
def solution(N):
    i=1
    c=0
    while i*i<N:
        if N%i==0:
            c+=2
        i+=1
    if i*i==N:
        c+=1
    return c
