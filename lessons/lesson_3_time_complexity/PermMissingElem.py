#method 1
def solution(A):
    set_A = set(A)
    N = len(A)
    set_B = set(range(1, N+2))
    return set_B.difference(set_A).pop()

#method 2
def solution(A):
    if len(A)==0:
        return 1
    A.sort()#O(NlogN)
    for i in range(len(A)):
        if A[i]!=i+1:
            return i+1
    return len(A)+1
