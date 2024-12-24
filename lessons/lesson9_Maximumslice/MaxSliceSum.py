#O(N)
def solution(A):
  #use max_end to store the max possible slice sum ending at some right index
  #use max_profit to store the global max slice sum
  #initialize max_end and the global max profit to be the first element
    max_end=max_profit=A[0]
    #iterate the right index Q of the slice from 1 to N-1
    for i in range(1,len(A)):
    #find the maximum possible sum of slice for each right index
    #for each right index i, the maximum possible sum of slice ending at that index can be represented as
    #max_end_i=max(max_end_(i-1)+A[i],A[i])
    #i.e., the maximal possible sum of slice end at i is A[i] itself when the maximal possible sum of slice end at (i-1) is negative; and it is the sum of the maximal possible sum of slice ends at (i-1) and A[i] when max_end_(i-1) is >=0
        max_end=max(A[i]+max_end,A[i])
    #update the global maximum slice sum to be the largest maximum sum for each right index
        max_profit=max(max_profit,max_end)
    return max_profit
