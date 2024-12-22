def solution(X, A):
    if len(A)<X:
        return -1
    #initialize an array to store the first time the position is cover by leaf
    #the first -1 is just a place holder
    ft=[-1]*(X+1)
  #store the first appearence tiem
    for i in range(len(A)):
        if ft[A[i]]==-1:
            ft[A[i]]=i
    m=0
    #start from the second element of ft since the first one is a placeholder
  #iterate to see whether there is -1, which means no leaf 
  #if no -1, which means all places are covered by leaves, then find the max time 
    for ele in ft[1:]:
        if ele == -1:
            return -1
        m=max(ele,m)
    return m
