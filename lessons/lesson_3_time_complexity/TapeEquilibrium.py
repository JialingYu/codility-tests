#time complexity O(N)
def solution(A):
    prefix_sums=[0]*(len(A)+1)
    #compute the prefix_sums where the first element is zero and the ith element is the sum of A[0]+...+A[i-1]
    for i in range(len(A)):
        prefix_sums[i+1]=prefix_sums[i]+A[i]
    #for 0<P<len(A), compute the absolute difference and get the min among them
    #initialize m to be the absolute difference when P=1
    m=abs(prefix_sums[1]-(prefix_sums[len(A)]-prefix_sums[1]))
    #iterate through P from 2 to len(A)-1
    for P in range(2,len(A)):
        #compute the absolute difference
        head=prefix_sums[P]
        tail=prefix_sums[len(A)]-prefix_sums[P]
        diff=abs(head-tail)
        m=min(m,diff)
    return m 
