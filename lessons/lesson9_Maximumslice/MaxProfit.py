#method 1:
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

#method 2:O(N)
def solution(A):
    if len(A)<=1:
        return 0
    #main idea:
    #the maximal profit of the whole period is the maximum among the maximal profit end at each day
    #to calculate the maximal profit end at day i, use the relation:
    #max_end_i=max(max_end_(i-1)+(A[i]-A[i-1]),A[i]-A[i-1])
    #i.e., if the maximal profit end at day i-1 is positive, the maximal profit end at day i would be the sum of maximal profit end at day i-1 and the profit of buying the stock at day i-1 and selling it at day i, otherwise it would be A[i]-A[i-1]
    max_profit=max_end=A[1]-A[0]
    for i in range(2,len(A)):
        max_end=max(max_end+(A[i]-A[i-1]),A[i]-A[i-1])
        max_profit=max(max_profit,max_end)
    if max_profit >0:
        return max_profit
    else:
        return 0
