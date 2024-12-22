def solution(A):
    #use prefix sum to count the number of cars moving west(has value 1) at position i
    prefix_sums=[0]*(len(A)+1)
    for i in range(1,len(A)+1):
        prefix_sums[i]=prefix_sums[i-1]+A[i-1]
    #use c to count the total numbe r of passing cars
    c=0
    #iterate through array A
    for i in range(len(A)):
    #if the value is zero, count the number of passing cars of it as the difference of the number of cars moving west at the end of the array 
    #and the number of it at current position
    
    #add the counting to c
    #if c > 1,000,000,000, break the for loop and return -1
    #return c
        if c > 1000000000:
            return -1
        if A[i]==0:
            c+=prefix_sums[-1]-prefix_sums[i]
    return c
