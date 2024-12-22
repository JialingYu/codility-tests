def solution(A, B, K):
    if K>B and A>0:
        return 0
    #since 0 is considered to be divisible by any integer other than 0 itself
    #if A==0, 0|K even if K>B
    if K>B and A==0:
        return 1
    #compute the quotient
    q_a=A//K
  #compute the remainder
    r_a=A%K
    q_b=B//K
  #if the remainder is zero, count add 1
    if r_a==0:
        return q_b-q_a+1
    else:
        return q_b-q_a
