#method 1:
#in python, set is implemented as a hash table as dictionary, and each key is mapped to a hash value by a hash map, 
#and the value is stored at that hash value position. Searching, inserting, and deleting is very efficient for hash table, which has average O(1)
#time complexity; but in worse case when many hash collisions(when the hash map generate the same hash value for different keys)
#occurs, complexity can be O(N)

def solution(A):
    s = set()
    for i in A:
      #searching in a set has O(1) time complexity
        if i in s:
          #deleting in a set has O(1) time complexity
          #set.remove(item), set.discard(item) will remove item inplace and return none
          #set.remove(item) will raise an error when the item is not in the set, but set.discard() will not
            s.remove(i)
        else:
            s.add(i)
          #set is unordered, set.pop() will return any element of the set
    return s.pop()

#method 2:
def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
  #use c to count the number of times an element appeared
    c=1
    for i in range(1,len(A)):
      #if the current element is not equal to the previous element and the previous element has appeared odd number of times
      #return the previous element
        if A[i]!=A[i-1] and c%2==1:
            return A[i-1]
      #if the current element is not equal to the previous element and the previous element has appeared even number of times
      #reset counting to 1 to count the appearence of current element
        elif A[i]!=A[i-1] and c%2==0:
            c=1
      #if the current element is equal to the previous element, continue the counting
        else:
            c+=1
    return A[-1]
  
#method 3,O(N) or O(N*log(N))
def solution(A):
    if len(A)==1:
        return A[0]
    A.sort()
    i=1
    while i <len(A):
      #if the current element is equal to the previous element
      #increment the index by 2
        if A[i]==A[i-1]:
            i+=2
      #otherwise return the previous element
        else:
            return A[i-1]
    #if the while loop has ended and the function do not return anything
    #this means the last element is the unpaired element and we should return it
    return A[-1]
