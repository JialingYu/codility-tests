#idea from: https://www.youtube.com/watch?v=BhBJ7MqjF-s&list=PLwEOixRFAUxZHuTDDgdmE0d4I40mBZLbF&index=22
#time complexity O(N)
def solution(H):
    if len(H)==1:
        return 1
    #use c to store the number of required blocks
    c=1
  #use re to store the heights of blocks which are reusable for the future
    re=[H[0]]
  #iterate through H
    for i in range(1,len(H)):
      #if the current height of the wall is smaller than the previous height
      #current height would act as a separator seperating the left and right part
      #the reusable blocks whose height is bigger than the height of the current wall would not be reusable anymore
      #since we can not connect these blocks to the right of the current wall
      #thus we need to remove them from re until no such blocks exists
      #if re is empty or the last element of re is not equal to the current height of the wall
      #increment c by 1 since we need one more block in this case and append current height of the wall to re since it can be reuse in the future
        if H[i]<H[i-1]:
            while len(re)>0 and re[-1]>H[i]:
                re.pop()
            if len(re)==0 or (len(re)>0 and re[-1]!=H[i]):
                c+=1
                re.append(H[i])
      #if the current height of the wall is bigger than the previous height
      #we need one more block and append current height for future reuse
        if H[i]>H[i-1]:
            re.append(H[i])
            c+=1
      #if the current height of the wall is equal to the previous height
  # we no nothing since we can extend the current block further
  
    return c
