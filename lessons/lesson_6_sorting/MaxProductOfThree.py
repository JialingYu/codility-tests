#time complexity O(NlogN)
def solution(A):
    if len(A)==3:
        return A[0]*A[1]*A[2]
    #sort A inplace
    #python list.sort() method use timesort and has time complexity O(NlogN)
    A.sort()
    #if all smaller than or equal to zero
    if A[-1]<=0:
        return A[-1]*A[-2]*A[-3]
    #if all bigger than or equal to zero
    elif A[0]>=0:
        return A[-1]*A[-2]*A[-3]
    #if some positive, some negative
    #either two smallest negative time one biggest positive or three biggest positive
    else:
        return max(A[0]*A[1]*A[-1],A[-1]*A[-2]*A[-3])
