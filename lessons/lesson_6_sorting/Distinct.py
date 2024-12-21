#time complexity O(NlogN) or O(N)
def solution(A):
    if len(A)==0:
        return 0
    #sort the array by ascending method
    #time complexity O(NlogN)
    #or we can use list.sort() method to sort the list in place
    A_sorted=sorted(A)
    #count the number of unique elements using the sorted array
    c=1
    for i in range(len(A_sorted)-1):
        if A_sorted[i+1]!=A_sorted[i]:
            c+=1
    return c
