def solution(A):
    #main idea:
    #iterate the array once, initialize the current max and min value to be the first element of the array
    #initialize max_prof to store the max profit
    #if the second element is bigger than the current max, update the max profit 
    #if the second element is smaller then the current min, update the current min and current max to be the second element
    #for other situations, do nothing
    l=len(A)
    if l < 2:
        return 0
    #initialize min_ max_ to be the first element
    min_= max_=A[0]
   #initialize the max profit to be zero
    max_prof=0
    for i in range(1,l):
        #if the current value bigger than max_
        #update the max_prof to be the bigger value between the current max_prof and A[i]-min_
        if A[i] > max_:
            max_prof=max(max_prof,A[i]-min_)
        #if the current value smaller than min_
        #update the min_ to be the current value
        #update max_ to be equal to min_
        elif A[i] < min_:
            min_=A[i]
            max_=min_
        #when current value is between min_ and max_, do nothing
    if max_prof <= 0:
        return 0
    return max_prof
