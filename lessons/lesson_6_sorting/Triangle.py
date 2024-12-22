#time complexity O(NlogN)
def solution(A):
    if len(A)<3:
        return 0
    #sort the array by ascending order
    A.sort()
    #iterate through the triples of the array
    for i in range(len(A)-2):
    #if the sum of the first two elements of the triple is bigger than the third element of the triple, this triple is valid for a triangle, return 1; if no such triple, return 0
        if A[i]+A[i+1]>A[i+2]:
            return 1
    return 0
