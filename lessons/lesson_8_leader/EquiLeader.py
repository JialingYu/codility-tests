#time complexity O(N)
def solution(A):
    if len(A)==1:
        return 0
    #if the left and right array of an equileader have the same leader, it must be the leader of the whole array A 
  #since the count of the leader would be more than half of the elements of A
    #thus if A has no leader, there is no equi leader
  
    def leader(a):
      '''a function to return the leader of an array, if no leader, return -1'''
        if len(a)==1:
            return a[0]
        #define a stack to eliminate the distinct elements of a
        #since only the same elements on the stack, we can only use the size and value to denote a stack
        size=0
        for i in range(len(a)):
            #if the stack is empty
            #append current value to the stack
            if size==0:
                size+=1
                value=a[i]
            #if the values of the stack is the same with current value, append it to the stack
            elif value==a[i]:
                size+=1
            #if the values of the stack is not the same with current value, remove the last value of the stack
            else:
                size-=1
        #if the final stack is empty, the array has no leader
        if size==0:
            return -1
        #otherwise the remaining elements which of the same value would be the candidate for the leader
        else:
            candidate=value
        #check whether the candidate is the leader
        c=0
        for i in range(len(a)):
            if a[i]==candidate:
                c+=1
        if c>len(a)/2:
            return candidate
        else:
            return -1

  #compute the leader of A
    L=leader(A)
    #print(L)
  #if L==-1, A has no leader, thus we have no equileader
    if L==-1:
        return 0
    #if A has leader, define a list to store the counting of the leader at every position
    leader_count=[0]*len(A)
    if A[0]==L:
        leader_count[0]=1
    for i in range(1,len(A)):
        if A[i]==L:
            leader_count[i]=leader_count[i-1]+1
        else:
            leader_count[i]=leader_count[i-1]
    #print(leader_count)
  
  #compute the sum of the equi leaders by checking every position, 
  #to see whether the counting of leader of its left and right array is bigger than a half of the corresponding array
    equi=0
    for p in range(len(A)-1):
        left=leader_count[p]
        right=leader_count[-1]-leader_count[p]
      #index p is an equileader when the counting of leader of its left and right array is bigger than a half of the corresponding array
        if left > (p+1)/2 and right > (len(A)-p-1)/2:
            equi +=1
    return equi
