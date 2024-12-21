#time complexity:O(N)
def solution(A, B):
    #use count to store the number of fishes get eaten
    count=0
    ds=[]
    # iterate through the direction array B
    for i in range(len(B)):
    #if direction is 1, append its index to list ds
        if B[i]==1:
            ds.append(i)
    #if direction is zero and the ds array is not empty, compare its size with the last element of ds, 
    #if the ds fish get eated, remove it from the list until ds is empty or the fish 0 gets eaten; 
    #add count by 1 when every fish get eaten
        while B[i]==0 and len(ds) >0:
            count+=1
            if A[i] > A[ds[-1]]:
                ds.pop()
            else:
                break
    #the remaining number of fishes is the total number of fishes minus the number of fishes get eaten
    return len(B)-count
