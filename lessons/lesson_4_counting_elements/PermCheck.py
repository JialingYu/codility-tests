#time complexity O(N) or O(NlogN)
def solution(A):
  #use c to store the appearance of elements of A
    c=[0]*(len(A)+1)
    for ele in A:
      #if element of A is within range and did not appear before
      #add the count by 1
        if ele <= len(A) and c[ele]==0:
            c[ele]+=1
        #if element of A is not within range or appeared before
      #not a permutation
        else:
            return 0
    return 1
